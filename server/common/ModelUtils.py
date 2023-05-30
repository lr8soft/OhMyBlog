from article_manager.models import Article, Reply
from user_manager.models import User

def GetArticle(id):
    try:
        return Article.objects.get(id=id)
    except:
        return None


def GetReply(id):
    try:
        return Reply.objects.get(id=id)
    except:
        return None