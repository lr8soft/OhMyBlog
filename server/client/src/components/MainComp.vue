<template>
    <div id="page">
        <div id="info-list">
            <div class="info-item" v-for="item in articleData" :key="item.id">
                <el-container class="info-item">
                    <el-header class="card-header" @click="navigateToArticle(item.id)">
                        <span class="card-text-single card-header-text">{{ item.title }}</span>
                    </el-header>

                    <el-main class="card-main">
                        <RichTextComp class="card-main-text" v-model="item.content" :editable="false"/>
                    </el-main>

                    <el-footer class="card-footer">
                        <span class="card-text-single card-footer-text">发表于{{ item.createDate }} &nbsp;{{ item.pageView }}次浏览</span>
                    </el-footer>
                </el-container>
            </div>
        </div>

        <div id="bottom-part">
            <el-pagination id="paginator-comp"
                v-model:current-page="currentPage"
                background
                layout="prev, pager, next, jumper"
                :page-count="pageCount"
                :page-size="pageItemCount"
                @current-change="handleCurrentChange"
            ></el-pagination>
        </div>

    </div>
</template>

<script>
import serviceApi from "@/services/serviceApi";
import {ElMessage} from "element-plus";
import {useGlobalData} from "@/services/globalData";
import RichTextComp from "@/components/RichTextComp.vue";
export default {
    name: "MainComp",
    components: {RichTextComp},
    data() {
        return {
            currentPage: 1,
            pageCount: 0,
            pageItemCount: 0,
            articleData: [
                {
                    id: 0,
                    title: 'title1',
                    content: '<p style="text-align: start;"><strong>dayjs是一个轻量的处理时间和日期的 JavaScript 库</strong></p><p style="text-align: start;"><strong>dayjs好处</strong></p><p style="text-align: start;"><br></p><ul><li style="text-align: start;">🕒 和Moment.js有着相同的API和模式</li><li style="text-align: start;">💪 不可变、持久性</li><li style="text-align: start;">🔥 提供链式调用</li><li style="text-align: start;">🌐 国际化标准</li><li style="text-align: start;">📦 超小的压缩体积，仅仅有2kb左右</li><li style="text-align: start;">👫 极大多数的浏览器兼容</li></ul>',
                    banner: "default.png",
                    pageView: 233,
                    createDate: "2021-01-01"
                },
                {
                    id: 1,
                    title: '222',
                    content: '<p>contentcontentcontentcontent</p>',
                    banner: "default.png",
                    pageView: 233,
                    createDate: "2021-01-01"
                }
            ],
            userData: useGlobalData()
        }
    },
    methods: {
        handleCurrentChange(val) {
            this.currentPage = val
            this.handlePageChange()
        },
        handlePageChange() {
            serviceApi.getTopicList(this.currentPage, this.pageItemCount).then(res => {
                this.topicData = res.data
                this.pageCount = res.pageCount
            }).catch(err => {
                ElMessage.error(err)
            })
        },
        navigateToArticle(id) {
            this.$router.push('/article/' + id)
        }
    }
}
</script>

<style scoped>
#page{
    width: 90%;
    min-height: 600rpx;
    margin: auto;
}

#info-list{
    width: 70%;
    min-height: 350px;
    margin: auto;
}

.info-item{
    width: 100%;
    /*min-width: 240px;*/
    border-radius: 5px;
    box-shadow: 0 1px 6px 0 rgba(0, 0, 0, 0.1);
    margin-top: 40px;
}

.card-header{
    width: 100%;
    height: 40px;
    margin: 20px auto 0 auto;
    /*下划线*/
    border-bottom: 1px solid #ebeef5;
}

.card-header-text{
    font-size: 18px;
}

.card-main{
    width: 100%;
    min-height: 150px;
    max-height: 450px;
    margin: 0 auto 0 auto;
    /*下划线*/
    border-bottom: 1px solid #ebeef5;
}

.card-text-single{
    text-align: left;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}

.card-main-text{
    /*最多换行3行，禁止滚动条*/
    /*overflow: hidden;
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    word-break: break-all;
    text-overflow: ellipsis;*/
    text-align: left;

    font-size: 15px;
}

.card-footer{
    width: 100%;
    height: 40px;
    margin: 20px auto 0 auto;
}

.card-footer-text{
    /*字体灰色*/
    color: #909399;
    font-size: 10px;
}

#bottom-part{
    width: 100%;
    height: 100px;
    margin: 20px auto;
}

#paginator-comp{
    width: 70%;
    margin: auto;
}
</style>