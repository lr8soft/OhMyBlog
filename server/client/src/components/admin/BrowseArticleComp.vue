<template>
    <el-card>
        <template #header>
            <span class="title-text">所有文章</span>
        </template>
        <el-table id="article-list" :data="articleList" height="250" style="width: 100%">
            <el-table-column prop="id" label="编号" width="180" />
            <el-table-column prop="title" label="标题" />
            <el-table-column label="创建时间"  width="240">
                <template #default="scope">
                    {{dayjs(scope.row.date).format("YYYY-MM-DD HH:mm:ss")}}
                </template>
            </el-table-column>
            <el-table-column label="操作">
                <template #default="scope">
                    <el-button
                        link type="primary"
                        @click='handleEditArticle(scope.row.id)'>编辑</el-button>
                    <el-button
                        link type="primary"
                        @click='handleDeleteArticle(scope.row.id)'>删除</el-button>
                </template>
            </el-table-column>
        </el-table>
    </el-card>
</template>

<script>
import {dayjs, ElMessage} from "element-plus";
import serviceApi from "@/services/serviceApi";

export default {
    name: "BrowseArticleComp",
    computed: {
        dayjs() {
            return dayjs
        }
    },
    mounted() {
        this.handleRequireArticleList()
    },
    data(){
        return {
            currentPage: 1,
            pageCount: 0,
            pageItemCount: 0,
            repliesCount: 2,
            articleList: [{
                id: 0,
                title: '这是标题',
                date: '2023-01-01 00:00:00'
            },{
                id: 1,
                title: '测试测试测测试测试测试测试测试测试测试测试测试测试测试测试试',
                date: '2000-01-01 00:00:00'
            }]
        }
    },
    methods: {
        handleRequireArticleList(){
            // 请求文章列表
            serviceApi.GetPaginationArticles(this.currentPage).then(res => {
                var result = serviceApi.GetApiResult(res)
                if(result){
                    this.articleList = res.result.data
                    this.pageItemCount = res.result.pageItemCount
                    this.pageCount = res.result.pageCount
                }else{
                    ElMessage.error(serviceApi.GetApiResultExplain(res))
                }

            }).catch(err => {
                ElMessage.error(err)
            })
        },
        handleEditArticle(id){
            console.log(id)
        },
        handleDeleteArticle(id){
            serviceApi.DeleteArticle(id).then(res => {
                var result = serviceApi.GetApiResult(res)
                if(result){
                    ElMessage.success("删除成功")
                    this.handleRequireArticleList()
                }else{
                    ElMessage.error(serviceApi.GetApiResultExplain(res))
                }
            }).catch(err => {
                ElMessage.error(err)
            })
        }
    }
}
</script>

<style scoped>
.title-text{
    font-size: 20px;
    font-weight: bold;
}

#article-list{
    width: 100%;
    min-height: 240px;
    margin: auto;
}
</style>