
import LoginComp from "@/components/LoginComp.vue";
import MainComp from "@/components/MainComp.vue";
import RegistComp from "@/components/RegistComp.vue";
import PageNotFoundComp from "@/components/PageNotFoundComp.vue";
import LogoutComp from "@/components/LogoutComp.vue";


const routes = [
    { path:'/', component: MainComp },
    { path:'/login', component: LoginComp },
    { path:'/regist', component: RegistComp },
    { path:'/logout', component: LogoutComp },
    // 最后匹配的就是404页面
    { path:'/:pathMatch(.*)', component: PageNotFoundComp }
]

export default routes