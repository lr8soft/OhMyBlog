<template>
    <el-container id="article-page">
        <el-header id="article-header">
            <span id="article-title-text">{{ articleInfo.title }}</span>
            <span id="article-detail-text">发表：{{articleInfo.createDate}}&nbsp;浏览量：{{articleInfo.pageView}}</span>
        </el-header>

        <el-main id="article-content">
            <RichTextComp id="article-content-text" v-model="articleInfo.content" :editable="false"/>
        </el-main>
    </el-container>

    <el-card id="article-page">
        <div  v-for="reply in replies" :key="reply.id">
            <el-container class="article-reply-item">
                <el-aside class="article-reply-user-info">
                    <el-icon size="64px"><User /></el-icon>
                </el-aside>
                <el-header>
                    <span>{{reply.user}}</span>
                </el-header>
                <el-main>
                    <span>{{reply.content}}</span>
                </el-main>
                <el-footer>
                    <span>{{reply.createData}}</span>
                </el-footer>
            </el-container>
        </div>
    </el-card>
</template>

<script>
import RichTextComp from "@/components/RichTextComp.vue";
import {dayjs} from "element-plus";
export default {
    name: "ArticleComp",
    components: {RichTextComp},
    computed: {
        dayjs() {
            return dayjs
        }
    },
    data() {
        return {
            articleInfo: {
                id: 0,
                title: 'DayJs',
                content: '<p style="text-align: start;"><strong>dayjs是一个轻量的处理时间和日期的 JavaScript 库</strong></p><p style="text-align: start;"><strong>dayjs好处</strong></p><p style="text-align: start;"><br></p><ul><li style="text-align: start;">🕒 和Moment.js有着相同的API和模式</li><li style="text-align: start;">💪 不可变、持久性</li><li style="text-align: start;">🔥 提供链式调用</li><li style="text-align: start;">🌐 国际化标准</li><li style="text-align: start;">📦 超小的压缩体积，仅仅有2kb左右</li><li style="text-align: start;">👫 极大多数的浏览器兼容</li></ul>',
                pageView: 233,
                createDate: "2021-01-01"
            },
            pageCount: 1,
            pageItemCount: 10,
            repliesCount: 1,
            replies: [
                {
                    id: 0,
                    user: 'lrsoft',
                    content: '测试回复',
                    createData: '2021-01-01 00:00:00'
                }
            ],
        }
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


.article-reply-item{
    width: 100%;
    min-height: 150px;
}

.article-reply-user-info{
    width: 120px;
    padding-top: 20px;
    align-items: center;
    text-align: center;
}
</style>