<template>
    <!--文章内容-->
    <el-container id="article-page">
        <el-header id="article-header">
            <span id="article-title-text">{{ articleInfo.title }}</span>
            <span id="article-detail-text">发表：{{dayjs(articleInfo.date).format("YYYY-MM-DD HH:mm:ss")}}&nbsp;浏览量：{{articleInfo.pageView}}</span>
        </el-header>

        <el-main id="article-content">
            <RichTextComp id="article-content-text" v-model="articleInfo.content" :editable="false"/>
        </el-main>
    </el-container>
    <!--评论区-->
    <el-card id="article-page">
        <span id="article-reply-count">共有{{repliesCount}}条回复</span>
        <div  v-for="reply in replies" :key="reply.id">
            <el-container class="article-reply">
                <el-aside class="article-reply-aside">
                    <img class="article-reply-user-avatar" :src="reply.avatar" @error="handleNoAvatar">
                    <!--如果头像加载失败-->
                    <p class="article-reply-username">{{reply.author}}</p>
                </el-aside>
                <el-main>
                    <span class="article-reply-content">{{reply.content}}</span>
                </el-main>
            </el-container>
        </div>
        <el-pagination id="article-paginator-comp"
                       v-model:current-page="currentPage"
                       background
                       layout="prev, pager, next, jumper"
                       :page-count="pageCount"
                       :page-size="pageItemCount"
                       @current-change="handleCurrentChange"
                       v-if="repliesCount > 0"
        ></el-pagination>
        <div id="article-create-reply">
            <textarea id="article-reply-textbox" v-model="formData.content" />
            <div id="article-reply-submit-area">
                <span id="article-reply-sum-text">当前回复总字数{{replyCharCount}}</span>
                <el-button id="article-reply-submit-btn" type="primary" @click="handleCreateReply">提交</el-button>
            </div>
        </div>
    </el-card>
</template>

<script>
import RichTextComp from "@/components/RichTextComp.vue";
import {dayjs, ElMessage} from "element-plus";
import serviceApi from "@/services/serviceApi";
import {useRoute} from "vue-router";
export default {
    name: "ArticleComp",
    components: {RichTextComp},
    computed: {
        dayjs() {
            return dayjs
        },
        replyCharCount() {
            return this.formData.content.length
        }
    },
    mounted() {
        const route = useRoute()
        var articleId = route.params.id
        this.articleInfo.id = articleId
        this.formData.articleId = articleId
        this.handleLoadArticle()
        this.handleLoadReplies()
    },
    data() {
        return {
            articleInfo: {
                id: 0,
                title: '',
                content: '',
                pageView: 0,
                date: "2021-01-01"
            },
            formData: {
                articleId: -1,
                content: ''
            },
            currentPage: 1,
            pageCount: 1,
            pageItemCount: 10,
            repliesCount: 0,
            replies: [],
            nullAvatar: require('../assets/avatar.jpg'),
        }
    },
    methods: {
        handleCreateReply() {
            serviceApi.CreateArticleReply(this.formData).then(res => {
                var result = serviceApi.GetApiResult(res)
                if(result){
                    this.handleLoadReplies()
                    this.formData.content = ''
                    ElMessage.success("发送成功")
                }else{
                    ElMessage.error(serviceApi.GetApiResultExplain(res))
                }
            })
        },
        handleLoadArticle() {
            serviceApi.GetArticleDetail(this.$route.params.id).then(res => {
                var result = serviceApi.GetApiResult(res)
                if(result){
                    this.articleInfo = res.result.data
                }else{
                    ElMessage.error(serviceApi.GetApiResultExplain(res))
                }
            })
        },
        handleLoadReplies() {
            serviceApi.GetArticleReplies(this.currentPage, this.articleInfo.id).then(res => {
                var result = serviceApi.GetApiResult(res)
                if(result){
                    this.replies = res.result.replies
                    this.repliesCount = this.replies.length
                    this.pageCount = res.result.pageCount
                }else{
                    ElMessage.error(serviceApi.GetApiResultExplain(res))
                }
            })
        },
        handleNoAvatar(e) {
            let img = e.srcElement;
            img.src = this.nullAvatar;
            img.onerror = null;
        },
    }
}
</script>

<style scoped>
#article-page{
    width: 60%;
    margin: 20px auto;

    border-radius: 5px;
    box-shadow: 0 1px 6px 0 rgba(0, 0, 0, 0.1);
}

#article-header{
    width: 100%;
    text-align: center;
    margin-top: 20px;

    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;

    flex-direction: column;
    display: flex;
}

#article-title-text{
    width: 100%;
    font-size: 28px;
    line-height: 30px;
    font-weight: bold;
}

#article-detail-text{
    width: 100%;
    font-size: 12px;
    line-height: 14px;
    color: #909399;

    margin-top: 10px;
}

#article-content{
    width: 100%;
    margin: 0 auto 20px auto;
}

#article-content-text{
    width: 100%;
    min-height: 300px;
    font-size: 16px;
}

#article-reply-count{
    font-size: 16px;
    font-weight: bold;
    margin: 10px auto 10px 5px;
}

.article-reply{
    margin: 10px auto 10px auto;
    border-bottom: 1px solid #ebeef5;
}

.article-reply-aside{
    width: 120px;
    /*height: 140px;*/
    padding-top: 10px;
    align-items: center;
    text-align: center;
    display: flex;
    flex-direction: column;
}

.article-reply-user-avatar{
    display: block;
    margin: 0 auto;
    width: 80px;
    height: 80px;
    border-radius: 50%;
}

.article-reply-username{
    margin-top: 15px;
    font-size: 14px;
}


.article-reply-content{
    font-size: 14px;
    min-height: 100px;
    word-break: break-all;
    word-wrap: break-word;
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-box-orient: vertical;

}

#article-paginator-comp{
    width: 100%;
    margin: auto auto 10px auto;
}


#article-create-reply{
    width: 100%;
    display: flex;
    flex-direction: column;
}

#article-reply-textbox{
    width: 100%;
    height: 100px;
    resize: none;
    border: 1px solid #ebeef5;
    border-radius: 1px;
    outline-color: #ebeef5;
}

#article-reply-submit-area{
    width: 100%;
    height: 50px;
    display: flex;
    flex-direction: row;
    margin: 5px auto 5px auto;
}

#article-reply-sum-text{
    font-size: 14px;
    color: #909399;
    margin-top: 5px;
    /*禁止换行 超长直接省略*/
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

#article-reply-submit-btn{
    margin-left: auto;
}

</style>