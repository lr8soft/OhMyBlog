<template>
    <div id="page">
        <div id="info-list">
            <div class="info-item" v-for="item in articleData" :key="item.id">
                <el-card>
                    <template #header>
                        <div class="card-header">
                            <span>{{item.title}}</span>
                        </div>
                    </template>
                    <div class="card-content">
                        <span>{{item.content}}</span>
                    </div>
                    <div class="card-footer">
                        <span>{{item.createDate}}</span>
                        <span>{{item.pageView}}次浏览</span>
                    </div>
                </el-card>
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
                    title: 'title1',
                    content: 'content1content1content1content1content1content1content1content1content1',
                    banner: "default.png",
                    pageView: 233,
                    createDate: "2021-01-01"
                },
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
    height: 350px;
    padding-bottom: 20px;
    margin: auto;
}

.info-item{
    width: 100%;
    margin: 20px auto 0 auto;
}

#bottom-part{
    width: 100%;
    height: 100px;
    margin: 20px auto;
}

#paginator-comp{
    width: 100%;
    margin: auto;
}
</style>