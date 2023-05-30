<template>
    <el-container id="page">
        <el-header id="header">
            <img :src="require('./assets/banner.jpg')" id="image-banner">
            <img :src="logo" id="image-logo">
        </el-header>
        <el-main id="main">
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
#app{
    margin: 0;
    padding: 0;
}

#page{
    height: 100%;
    width: 100%;
}

#header{
    width: 100%;
    height: 300px;
}

#image-banner{
    width: 100%;
    height: 300px;
    object-fit: cover;
    position: absolute;
    margin: 0;
    padding: 0;
    top: 0;
    left: 0;
    right: 0;
}

#image-logo{
    position: relative;
    width: 128px;
    height: 128px;
    object-fit: fill;
    margin: auto;
}

#main{
    width: 100%;
    padding: 0;
}
</style>