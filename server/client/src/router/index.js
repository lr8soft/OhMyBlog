import {createRouter, createWebHistory} from "vue-router";
import routes from "@/router/routers";
import {useGlobalData} from "@/services/globalData";

const router = createRouter({
    routes: routes,
    history: createWebHistory(process.env.BASE_URL)
})

// router拦截是否管理员
router.beforeEach((to, from, next) => {
    if (to.meta.requiresAuth) {
        if (!useGlobalData().isAdmin) {
            next({
                path: "/login",
                query: {redirect: to.fullPath}
            })
        } else {
            next()
        }
    } else {
        next()
    }
})

export default router