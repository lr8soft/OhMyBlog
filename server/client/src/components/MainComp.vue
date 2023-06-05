<template>
    <div id="page">
        <div id="info-list">
            <div class="info-item" v-for="item in articleData" :key="item.id">
                <el-container class="info-item">
                    <el-header class="card-header" @click="navigateToArticle(item.id)">
                        <span class="card-text-single card-header-text">{{ item.title }}</span>
                    </el-header>

                    <el-main class="card-main">
                        <RichTextComp class="card-main-text" v-model="item.content" :editable="false" :scrollable="false"/>
                    </el-main>

                    <el-footer class="card-footer">
                        <span class="card-text-single card-footer-text">发表于{{dayjs(item.date).format("YYYY-MM-DD HH:mm:ss")}} &nbsp;{{ item.pageView }}次浏览</span>
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
import {dayjs, ElMessage} from "element-plus";
import {useGlobalData} from "@/services/globalData";
import RichTextComp from "@/components/RichTextComp.vue";
export default {
    name: "MainComp",
    components: {RichTextComp},
    computed: {
        dayjs() {
            return dayjs
        }
    },
    mounted() {
        this.handlePageChange()
    },
    data() {
        return {
            currentPage: 1,
            pageCount: 0,
            pageItemCount: 0,
            articleData: [
                {
                    id: 0,
                    title: '',
                    content: '',
                    pageView: 0,
                    date: "2021-01-01"
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
            serviceApi.GetPaginationArticles(this.currentPage).then(res => {
                var result = serviceApi.GetApiResult(res)
                if(result){
                    this.articleData = res.result.data
                    this.pageItemCount = res.result.pageItemCount
                    this.pageCount = res.result.pageCount
                }else{
                    ElMessage.error(serviceApi.GetApiResultExplain(res))
                }

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
    min-height: 600px;
    margin: auto;
}

#info-list{
    width: 68%;
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
    min-height: 150px;
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