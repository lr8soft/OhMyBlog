<template>
    <el-container id="app-page">
        <el-header id="app-header">
            <img :src="require('./assets/banner.jpg')" id="app-image-banner">
            <img :src="logo" id="app-image-logo">

            <div id="app-menu-btn-group">
                <el-icon id="app-menu-icon" size="32" color="gray"><Menu /></el-icon>
                <el-icon id="app-search-icon" size="32" color="gray"><Stopwatch /></el-icon>
            </div>

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
    -webkit-transform: translate(-50%, -50%) rotate(360deg);
    -moz-transform: translate(-50%, -50%) rotate(360deg);
    -o-transform: translate(-50%, -50%) rotate(360deg);
}

#app-menu-btn-group{
    position: relative;
    width: 48px;
    margin: 32px 32px auto auto;
    flex-direction: column;
    display: flex;
}

#app-menu-icon{
    width: 48px;
    height: 48px;
    border-radius: 5%;
    background-color: white;
    cursor: pointer;
}

#app-search-icon{
    width: 48px;
    height: 48px;
    border-radius: 5%;
    background-color: white;
    margin-top: 16px;
    cursor: pointer;
}

#app-main{
    width: 100%;
    padding: 0;
}
</style>