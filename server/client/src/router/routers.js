
import LoginComp from "@/components/LoginComp.vue";
import MainComp from "@/components/MainComp.vue";
import RegistComp from "@/components/RegistComp.vue";


const routes = [
    { path:'/', component: MainComp },
    { path:'/login', component: LoginComp },
    { path:'/regist', component: RegistComp },
    // 最后匹配的就是404页面
    //{ path:'/:pathMatch(.*)', component: PageNotFoundComp }
]

export default routes