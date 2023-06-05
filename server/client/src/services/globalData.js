import {defineStore} from "pinia";
export const useGlobalData = defineStore('globaldata',{
    state: () => ({
        is_login: false,
        is_admin: false,
        user_name: ''
    }),
    persist: {
        enabled: true,
        strategies: [{
            storage: localStorage,
            paths: ['is_login'],
            key: "is_login"
        }, {
            storage: sessionStorage,
            paths: ['is_login'],
            key: "is_login"
        }, {
            storage: localStorage,
            paths: ['user_name'],
            key: "user_name"
        }, {
            storage: sessionStorage,
            paths: ['user_name'],
            key: "user_name"
        }, {
            storage: localStorage,
            paths: ['is_admin'],
            key: "is_admin"
        }, {
            storage: sessionStorage,
            paths: ['is_admin'],
            key: "is_admin"
            }
        ],
    },
    getters: {
        isLogin: (state) => state.is_login,
        isAdmin: (state) => state.is_admin,
        userName: (state) => state.user_name
    },
    actions: {
        setIsLogin(value){
            this.is_login = value
        },
        setIsAdmin(value){
            this.is_admin = value
        },
        setUserName(value){
            this.user_name = value
        }
    }
})