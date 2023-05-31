<template>
    <el-container id="app-page">
        <el-header id="app-header">
            <img :src="require('./assets/banner.jpg')" id="app-image-banner">
            <img :src="logo" id="app-image-logo">
        </el-header>
        <el-main id="app-main">
            <router-view></router-view>
        </el-main>
    </el-container>
</template>

<script>
import {useGlobalData} from "@/services/globalData";
export default {
    name: 'App',
    data(){
        return{
            logo: require('./assets/logo.png'),
            userData: useGlobalData()
        }
    }
}
</script>
<style>
html, body{
    margin: 0;
    padding: 0;
}

#app-page{
    height: 100%;
    width: 100%;
}

#app-header{
    width: 100%;
    height: 300px;
    position: relative;
    margin: 0;
    padding: 0;
}

#app-image-banner{
    width: 100%;
    height: 300px;
    object-fit: cover;
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
}

#app-image-logo{
    width: 128px;
    height: 128px;
    background-color: whitesmoke;
    object-fit: fill;
    /*居中*/
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    /*圆形外框*/
    border-radius: 50%;
    border: 2px solid white;
    /*旋转动画时间*/
    transition: All 0.6s ease-in-out;
    -webkit-transition: All 0.6s ease-in-out;
    -moz-transition: All 0.6s ease-in-out;
    -o-transition: All 0.6s ease-in-out;
}

#app-image-logo:hover{
    transform: translate(-50%, -50%) rotate(360deg);
}

#app-main{
    width: 100%;
    padding: 0;
}
</style>