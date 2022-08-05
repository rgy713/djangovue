import {createWebHistory, createRouter} from "vue-router";
import Home from "@/views/Home.vue";
import Signup from "@/views/Signup.vue";
import Login from "@/views/Login.vue";
import UserCenter from "@/views/UserCenter.vue";
import SendMessage from "@/views/SendMessage.vue";

const routes = [
    {
        path: "/",
        name: "Home",
        component: Home,
    },
    {
        path: "/signup",
        name: "Signup",
        component: Signup
    },
    {
        path: "/login",
        name: "Login",
        component: Login
    },
    {
        path: "/user/:username",
        name: "UserCenter",
        component: UserCenter
    },
    {
        path: "/message/create",
        name: "SendMessage",
        component: SendMessage
    },
];

const router = createRouter({
    // https://next.router.vuejs.org/guide/essentials/history-mode.html
    history: createWebHistory(),
    routes,
});

export default router;