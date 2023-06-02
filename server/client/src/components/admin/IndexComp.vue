<template>
    <el-card id="admin-index-comp">
        <template #header>
            <span id="title-text">OhMyBlog后台管理</span>
        </template>

    </el-card>
</template>

<script>
export default {
    name: "IndexComp"
}
</script>

<style scoped>
#admin-index-comp{
    width: 100%;
    height: 450px;
}

#title-text{
    font-size: 20px;
    font-weight: bold;
}
</style>