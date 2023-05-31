<template>
    <div id="page">
        <div id="info-list">
            <div class="info-item" v-for="item in articleData" :key="item.id">
                <el-container class="info-item">
                    <el-header class="card-header">
                        <span class="card-text-single card-header-text">{{ item.title }}</span>
                    </el-header>

                    <el-main class="card-main">
                        <span class="card-main-text">{{ item.content }}</span>
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

export default {
    name: "MainComp",
    data() {
        return {
            currentPage: 1,
            pageCount: 0,
            pageItemCount: 0,
            articleData: [
                {
                    id: 0,
                    title: 'title1',
                    content: 'content1content1content1ccontent1content1content1content1content1content1content1content1content1ontent1content1content1content1content1content1',
                    banner: "default.png",
                    pageView: 233,
                    createDate: "2021-01-01"
                },
                {
                    id: 1,
                    title: '222',
                    content: 'sfasfsfsdfjsadlfjlksdflksdlsfjdsfsflsjfslkfjssldkdjflksdjlfsldjkfl',
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
    height: 150px;
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
    overflow: hidden;
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    text-overflow: ellipsis;
    text-align: left;
    word-break: break-all;

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