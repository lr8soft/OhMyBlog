from django.core.paginator import Paginator
from django.views.decorators.http import require_http_methods

from article_manager.models import Article, Reply
from common import SessionUtils, CommonEnum, ModelUtils, StringUtils
from common.ResponseUtils import EnumResponse
from core import settings


@require_http_methods(['POST'])
def create_new_reply(request):
    response = EnumResponse()
    # 检测是否登录
    if not SessionUtils.IsLogin(request):
        response.setStatus(CommonEnum.ErrorResponse.NOT_LOGIN)
        return response.getResponse()

    articleId = request.POST.get("articleId")
    content = request.POST.get("content")
    # 检测输入是否完整
    if not articleId or not content:
        response.setStatus(CommonEnum.ErrorResponse.INCOMPLETE_DATA)
        return response.getResponse()

    # 转义HTML标签
    content = StringUtils.ConvertToWebString(content)
    user = SessionUtils.GetUser(request)

    article = ModelUtils.GetArticle(articleId)
    # 检测文章是否存在
    if not article:
        response.setStatus(CommonEnum.ErrorResponse.ARTICLE_NOT_EXIST)
        return response.getResponse()

    try:
        Reply.objects.create(author=user, content=content, article=article)

        article.repliesCount += 1
        article.save()
    except Exception as error:
        response.setStatus(CommonEnum.ErrorResponse.OPERATION_FAIL)
        print(error)

    return response.getResponse()


@require_http_methods(['POST'])
def get_pagination_replies(request):
    response = EnumResponse()
    # 页码默认是1
    pageNum = request.POST.get("pageNum")
    articleId = request.POST.get("articleId")

    # 检测输入完整
    if not pageNum or not pageNum.isdigit() or not articleId:
        response.setStatus(CommonEnum.ErrorResponse.INCOMPLETE_DATA)
        return response.getResponse()

    pageNum = int(pageNum)

    article = ModelUtils.GetArticle(articleId)
    # 检测文章是否存在
    if not article:
        response.setStatus(CommonEnum.ErrorResponse.ARTICLE_NOT_EXIST)
        return response.getResponse()

    try:
        paginator = Paginator(Reply.objects.filter(article=article), settings.PAGINATOR_ITEM_PER_PAGE)
        pageCount = paginator.num_pages
        # 检测页码是否超出范围,[1,n]
        if pageNum < 1 or pageNum > pageCount:
            response.setStatus(CommonEnum.ErrorResponse.PAGE_OUT_OF_RANGE)
            return response.getResponse()
        # 读指定页的所有内容
        result = {}
        result["pageCount"] = pageCount
        result["pageItemCount"] = settings.PAGINATOR_ITEM_PER_PAGE

        result["replies"] = []
        page = paginator.page(pageNum)
        for reply in page:
            # 解析所有replies
            result["replies"].append({
                "id": reply.id,
                "author": reply.author.username,
                "content": reply.content,
                "date": reply.date,
                "avatar": ""
            })

        response.setResult(result)
    except Exception as error:
        response.setStatus(CommonEnum.ErrorResponse.OPERATION_FAIL)
        print(error)

    return response.getResponse()