<template>
    <div id="admin-page">
        <el-card id="left-float-card">
            <el-menu
                default-active="1"
                id="admin-menu">
                <el-sub-menu index="1">
                    <template #title>
                        <el-icon><Document /></el-icon>
                        <span>文章管理</span>
                    </template>
                    <el-menu-item index="1-1" @click="compIndex=1">新建文章</el-menu-item>
                    <el-menu-item index="1-2" @click="compIndex=2">所有文章</el-menu-item>
                </el-sub-menu>
                <el-sub-menu index="2">
                    <template #title>
                        <el-icon><User /></el-icon>
                        <span>用户管理</span>
                    </template>
                    <el-menu-item index="2-1" @click="compIndex=3">用户列表</el-menu-item>
                </el-sub-menu>
                <el-sub-menu index="3">
                    <template #title>
                        <el-icon><Compass /></el-icon>
                        <span>导航管理</span>
                    </template>
                    <el-menu-item index="3-1">右导航栏管理</el-menu-item>
                </el-sub-menu>
            </el-menu>
        </el-card>

        <keep-alive>
            <component id="admin-card" :is="currentAdminComp"></component>
        </keep-alive>
    </div>
</template>

<script>
import NewArticleComp from "@/components/admin/NewArticleComp.vue";
import BrowseArticleComp from "@/components/admin/BrowseArticleComp.vue";
import IndexComp from "@/components/admin/IndexComp.vue";
import BrowseUserComp from "@/components/admin/BrowseUserComp.vue";

export default {
    name: "AdminComp",
    components: {IndexComp, NewArticleComp, BrowseArticleComp, BrowseUserComp},
    computed:{
        currentAdminComp(){
            return this.compList[this.compIndex]
        }
    },
    data() {
        return {
            compIndex: 0,
            compList: ['IndexComp', 'NewArticleComp', 'BrowseArticleComp', 'BrowseUserComp'],
        }
    }
}
</script>

<style scoped>
#admin-page{
    width: 100%;
    height: 800px;
    display: flex;
    flex-direction: row;
}
/*靠左显示不固定*/
#left-float-card{
    width: 200px;
    min-width: 190px;
    float: left;
    margin: 20px 0 auto 20px;
}

#admin-menu{
    /*width: 100%;*/
    height: 150px;
    height: 100%;
    border: none;
}

#admin-card{
    /*width: 90%;
    min-width: 750px;
    min-height: 500px;*/
    width: 100%;
    margin: 20px 20px auto 20px;
}
</style>