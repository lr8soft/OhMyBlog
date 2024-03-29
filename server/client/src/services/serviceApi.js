import requestHelper from "@/services/requestHelper";

let urlHead = "/api";
export default {
    TryLogin(formData){
        return requestHelper({
            url: urlHead + "/user/login",
            method: "post",
            data: formData
        })
    },

    TryRegist(formData){
        return requestHelper({
            url: urlHead + "/user/regist",
            method: "post",
            data: formData
        })
    },
    GoLogout(){
        return requestHelper({
            url: urlHead + "/user/logout",
            method: "post"
        })
    },
    GetPaginationArticles(pageNum){
        return requestHelper({
            url: urlHead + "/article/get_pagination_articles",
            method: "post",
            data: {pageNum: pageNum}
        })
    },
    CreateNewArticle(formData){
        return requestHelper({
            url: urlHead + "/article/create_new_article",
            method: "post",
            data: formData
        })
    },
    DeleteArticle(articleId){
        return requestHelper({
            url: urlHead + "/article/delete_article",
            method: "post",
            data: { id: articleId }
        })
    },
    GetArticleDetail(articleId){
        return requestHelper({
            url: urlHead + "/article/get_article_detail",
            method: "post",
            data: { id: articleId }
        })
    },

    GetApiResult(response){
        if(response.status === "operation_success")
            return true
        return false
    },
    GetApiResultExplain(response){
        if(response.status in statusExplain)
            return statusExplain[response.status]
        return "未知错误"
    },

}


var statusExplain = {
    "not_login": "用户未登录",
    "incomplete_certificate": "用户凭据不完整",
    "wrong_certificate": "用户凭据有误",
    "user_existed": "用户已经存在" ,
    "user_not_exist": "用户不存在",
    "permission_denied": "权限不足",
    "no_upload_file": "未上传文件" ,
    "file_not_exist": "文件不存在" ,
    "user_no_project": "用户并未参与项目" ,
    "operation_success": "操作成功" ,
    "operation_fail": "操作失败",
    "incomplete_data": "输入数据不完整",
    "parse_error": "服务器响应格式有误" ,
    "invalid_argument": "参数错误" ,
    "reply_not_exist": "回复不存在",
    "topic_not_exist": "帖子不存在",
    "page_out_of_range": "页码超出范围",
    "can_not_delete_theme_content": "无法删除主题内容"
}
