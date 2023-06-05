from django.core.paginator import Paginator
from django.views.decorators.http import require_http_methods

from article_manager.models import Article
from common import SessionUtils, CommonEnum, ModelUtils
from common.ResponseUtils import EnumResponse
from core import settings


# Create your views here.
@require_http_methods(['POST'])
def create_new_article(request):
    response = EnumResponse()
    # 检测是否登录
    if not SessionUtils.IsLogin(request):
        response.setStatus(CommonEnum.ErrorResponse.NOT_LOGIN)
        return response.getResponse()

    title = request.POST.get("title")
    content = request.POST.get("content")
    # 检测输入是否完整
    if not title or not content:
        response.setStatus(CommonEnum.ErrorResponse.INCOMPLETE_DATA)
        return response.getResponse()

    user = SessionUtils.GetUser(request)

    try:
        newArticle = Article.objects.create(author=user, title=title, content=content, repliesCount=0, pageView=0)
    except Exception as error:
        response.setStatus(CommonEnum.ErrorResponse.OPERATION_FAIL)
        print(error)

    return response.getResponse()


@require_http_methods(['POST'])
def get_pagination_articles(request):
    response = EnumResponse()
    # 页码默认是1
    pageNum = request.POST.get("pageNum")
    # 检测输入完整
    if not pageNum or not pageNum.isdigit():
        response.setStatus(CommonEnum.ErrorResponse.INCOMPLETE_DATA)
        return response.getResponse()

    pageNum = int(pageNum)

    try:
        paginator = Paginator(Article.objects.all(), settings.PAGINATOR_ITEM_PER_PAGE)
        pageCount = paginator.num_pages
        # 检测页码是否超出范围,[1,n]
        if pageNum < 1 or pageNum > pageCount:
            response.setStatus(CommonEnum.ErrorResponse.PAGE_OUT_OF_RANGE)
            return response.getResponse()

        result = {}
        result["pageCount"] = pageCount
        result["pageItemCount"] = settings.PAGINATOR_ITEM_PER_PAGE
        # 读指定页的所有内容
        page = paginator.page(pageNum)
        pageTopics = []
        for article in page:
            info = {"id": article.id, "title": article.title,
                    "content": article.content, "author": article.author.username,
                    "repliesCount": article.repliesCount, "pageView": article.pageView,
                    "date": article.date}
            pageTopics.append(info)

        result["data"] = pageTopics
        response.setResult(result)

    except Exception as error:
        response.setStatus(CommonEnum.ErrorResponse.OPERATION_FAIL)
        print("get_pagination_topics ERROR:" + error.__str__())

    return response.getResponse()


@require_http_methods(['POST'])
def get_article_detail(request):
    response = EnumResponse()
    # 检测输入完整
    articleId = request.POST.get("id")
    if not articleId:
        response.setStatus(CommonEnum.ErrorResponse.INCOMPLETE_DATA)
        return response.getResponse()

    # 文章是否存在
    article = ModelUtils.GetArticle(articleId)
    if not article:
        response.setStatus(CommonEnum.ErrorResponse.ARTICLE_NOT_EXIST)
        return response.getResponse()

    result = {"data": {
        "id": article.id,
        "title": article.title,
        "content": article.content,
        "author": article.author.username,
        "repliesCount": article.repliesCount,
        "pageView": article.pageView,
        "date": article.date
    }}

    try:
        article.pageView += 1
        article.save()
    except Exception as error:
        print(error)

    response.setResult(result)

    return response.getResponse()


@require_http_methods(['POST'])
def delete_article(request):
    response = EnumResponse()
    # 检测是否登录
    if not SessionUtils.IsLogin(request):
        response.setStatus(CommonEnum.ErrorResponse.NOT_LOGIN)
        return response.getResponse()

    # 是否管理员
    if not SessionUtils.GetIsAdmin(request):
        response.setStatus(CommonEnum.ErrorResponse.PERMISSION_DENIED)
        return response.getResponse()

    # 检测输入完整
    articleId = request.POST.get("id")
    if not articleId:
        response.setStatus(CommonEnum.ErrorResponse.INCOMPLETE_DATA)
        return response.getResponse()

    # 文章是否存在
    article = ModelUtils.GetArticle(articleId)
    if not article:
        response.setStatus(CommonEnum.ErrorResponse.ARTICLE_NOT_EXIST)
        return response.getResponse()

    try:
        article.delete()
    except Exception as error:
        response.setStatus(CommonEnum.ErrorResponse.OPERATION_FAIL)
        print(error)

    return response.getResponse()
