<template>
  <form class="regist-form">
  <p>新用户注册</p>
  <div class="regist-form-item">
    <el-input v-model="formData.username" placeholder="用户名" size="large"/>
  </div>
  <div class="regist-form-item">
    <el-input v-model="formData.password" placeholder="密码" type="password" size="large"/>
  </div>
    <div class="regist-form-item">
      <el-input v-model="formData.nickname" placeholder="呢称" size="large"/>
    </div>
  <div class="regist-form-item">
      <el-input v-model="formData.email" placeholder="电子邮箱" size="large"/>
  </div>
  <el-button type="primary" @click="onSubmit" size="large">注册</el-button>
  </form>
</template>
<script>
import serviceApi from "@/services/serviceApi";
import {ElMessage} from "element-plus";
export default {
  name: "RegistComp",
  data(){
    return{
      formData: {
        username: '',
        password: '',
        email: '',
        nickname:''
      }
    }
  },
  methods:{
    onSubmit(){
      serviceApi.TryRegist(this.formData)
          .then(response=>{
            if(serviceApi.GetApiResult(response)){
              ElMessage({
                message: '注册成功',
                type: 'success'
              })
              this.$router.push('/login')
            }else{
              ElMessage({
                message: serviceApi.GetApiResultExplain(response),
                type: 'error'
              })
            }

          })
    }
  }
}
</script>

<style scoped>
.regist-form{
  width: 400px;
  height: 400px;
  margin: 40px auto;
  text-align: center;
  border-radius: 10px;
  border: 1px solid var(--el-border-color);
  box-shadow: var(--el-box-shadow-dark);
}
.regist-form-item{
  width: 84%;
  margin-left: 8%;
  margin-right: 8%;
  margin-bottom: 18px;
}

p{
  font-size: 28px;
}
</style>