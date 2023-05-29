<template>
    <div id="thread-body">
        <div id="info-list">
            <p>MainPage</p>
        </div>

        <div style="margin: 10px 0">
            <el-pagination
                v-model:current-page="currentPage"
                background
                layout="prev, pager, next, jumper"
                :page-count="pageCount"
                :page-size="pageItemCount"
                @current-change="handleCurrentChange"
            />
        </div>
    </div>
</template>

<script>
export default {
    name: "MainComp",
    data() {
        return {
            currentPage: 1,
            pageCount: 0,
            pageItemCount: 0
        }
    }
}
</script>

<style scoped>
#info-list{
    width: 70%;
    height: 350px;
}
</style>