
import LoginComp from "@/components/LoginComp.vue";
import MainComp from "@/components/MainComp.vue";
import RegistComp from "@/components/RegistComp.vue";
import PageNotFoundComp from "@/components/PageNotFoundComp.vue";
import LogoutComp from "@/components/LogoutComp.vue";
import ArticleComp from "@/components/ArticleComp.vue";
import AdminComp from "@/components/AdminComp.vue";


const routes = [
    { path: '/', component: MainComp },
    { path: '/login', component: LoginComp },
    { path: '/regist', component: RegistComp },
    { path: '/logout', component: LogoutComp },
    { path: '/article/:id', component: ArticleComp },
    { path: '/admin', component: AdminComp,/* meta: { requiresAuth: true }*/ },
    // 最后匹配的就是404页面
    { path: '/:pathMatch(.*)', component: PageNotFoundComp }
]

/*routes.beforeEach((from, to , next) => {
    if (to.meta.requiresAuth) {
        if (!localStorage.getItem('token')) {
            next({
                path: '/login',
                query: { redirect: to.fullPath }
            })
        } else {
            next()
        }
    } else {
        next()
    }
})*/

export default routes