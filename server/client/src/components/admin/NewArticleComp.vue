<template>
    <el-card id="new-article-comp">
        <template #header>
            <span class="title-text">新建文章</span>
        </template>
        <div id="content-block">
            <el-input id="content-title" v-model="formData.title" placeholder="文章标题" />
            <RichTextComp id="content-text" v-model="formData.content" :editable="true"/>
            <div id="content-button-list">
                <el-button size="large" type="primary" @click="handleSubmitArticle">发布</el-button>
                <el-button size="large" type="info" @click="handleTempSave">保存草稿</el-button>
            </div>
        </div>
    </el-card>
</template>

<script>
import RichTextComp from "@/components/RichTextComp.vue";
import {ElMessage} from "element-plus";

export default {
    name: "NewArticleComp",
    components: {RichTextComp},
    data(){
        return {
            formData: {
                title: '',
                content: ''
            }
        }
    },
    methods: {
        handleSubmitArticle(){

        },

        handleTempSave(){
            ElMessage({
                message: '保存成功',
                type: 'success'
            })
        }
    }
}
</script>

<style scoped>
#new-article-comp{
    width: 100%;
    min-width: 750px;
    height: 500px;

}

.title-text{
    font-size: 20px;
    font-weight: bold;
}

#content-block{
    width: 100%;
    display: flex;
    flex-direction: column;
}

#content-title{
    width: 100%;
    font-size: 16px;
}

#content-text{
    width: 100%;
    height: 400px;
    text-align: left;
    font-size: 15px;
    margin: 10px auto;
}

#content-button-list{
    width: 100%;
    display: flex;
    flex-direction: row;
}
</style>