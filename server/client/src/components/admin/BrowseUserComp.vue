<template>
    <el-card id="browse-user-comp">
        <template #header>
            <span id="title-text">用户列表</span>
        </template>
        <el-table id="user-list" :data="userList" height="250" style="width: 100%">
            <el-table-column prop="id" label="ID" width="180" />
            <el-table-column prop="username" label="用户名" />
            <el-table-column prop="isAdmin" label="是否管理员" />
            <el-table-column label="操作">
                <template #default="scope">
                    <el-button
                        link type="primary"
                        @click='handleEditUser(scope.row.id)'>编辑</el-button>
                    <el-button
                        link type="primary"
                        @click='handleDeleteUser(scope.row.id)'>删除</el-button>
                </template>
            </el-table-column>
        </el-table>
    </el-card>
</template>

<script>
export default {
    name: "BrowserUserComp",
    mounted() {
        this.handleRequireUserList()
    },
    data(){
        return {
            userList: [
                {
                    id: 0,
                    username: 'test',
                    isAdmin: false
                },
                {
                    id: 1,
                    username: 'lrsoft',
                    isAdmin: true
                }
            ]
        }
    },
    methods: {
        handleRequireUserList(){
            // 请求用户列表
        },
        handleEditUser(id){
            console.log(id)
        },
        handleDeleteUser(id){
            console.log(id)
        }
    }
}
</script>

<style scoped>
#browse-user-comp{
    width: 100%;
}

#title-text{
    font-size: 20px;
    font-weight: bold;
}

#user-list{
    width: 100%;
    min-height: 240px;
    margin: auto;
}
</style>