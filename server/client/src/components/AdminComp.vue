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
                    <el-menu-item index="1-1">新建文章</el-menu-item>
                    <el-menu-item index="1-2">编辑文章</el-menu-item>
                </el-sub-menu>
                <el-sub-menu index="2">
                    <template #title>
                        <el-icon><User /></el-icon>
                        <span>用户管理</span>
                    </template>
                    <el-menu-item index="2-1">用户列表</el-menu-item>
                    <el-menu-item index="2-2">用户评论</el-menu-item>
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

        <el-card id="admin-card">

        </el-card>
    </div>
</template>

<script>
export default {
    name: "AdminComp"
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
    width: 90%;
    min-width: 750px;
    min-height: 500px;
    margin: 20px 20px auto 20px;
}
</style>