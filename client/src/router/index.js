import {createRouter, createWebHistory} from "vue-router";
import Home from "../views/Home.vue";

const routes = [
    {
        path: '/',
        redirect: '/dashboard'
    }, {
        path: "/",
        name: "Home",
        component: Home,
        children: [
            {
                path: "/dashboard",
                name: "dashboard",
                meta: {
                    title: 'Home'
                },
                component: () => import (
                /* webpackChunkName: "dashboard" */
                "../views/Dashboard.vue")
            }, {
                path: "/resources",
                name: "basetable",
                meta: {
                    title: 'Resources'
                },
                component: () => import (
                /* webpackChunkName: "table" */
                "../views/Resources.vue")
            }, {
                path: "/reservations",
                name: "reservations",
                meta: {
                    title: 'Reservations'
                },
                component: () => import (
                /* webpackChunkName: "table" */
                "../views/Reservations.vue")
            }, {
                path: "/data",
                name: "basecharts",
                meta: {
                    title: 'Dashboard'
                },
                component: () => import (
                /* webpackChunkName: "charts" */
                "../views/BaseCharts.vue")
            }, {
                path: "/add",
                name: "addResource",
                meta: {
                    title: 'Add'
                },
                component: () => import (
                /* webpackChunkName: "form" */
                "../views/AddResource.vue")
            }, {
                path: "/messages",
                name: "tabs",
                meta: {
                    title: 'Messages'
                },
                component: () => import (
                /* webpackChunkName: "tabs" */
                "../views/Tabs.vue")
            }, {
                path: "/permission",
                name: "permission",
                meta: {
                    title: '????????????',
                    permission: true
                },
                component: () => import (
                /* webpackChunkName: "permission" */
                "../views/Permission.vue")
            }, {
                path: "/i18n",
                name: "i18n",
                meta: {
                    title: '?????????'
                },
                component: () => import (
                /* webpackChunkName: "i18n" */
                "../views/I18n.vue")
            }, {
                path: "/upload",
                name: "upload",
                meta: {
                    title: 'Upload'
                },
                component: () => import (
                /* webpackChunkName: "upload" */
                "../views/Upload.vue")
            }, {
                path: "/icon",
                name: "icon",
                meta: {
                    title: '??????'
                },
                component: () => import (
                /* webpackChunkName: "icon" */
                "../views/Icon.vue")
            }
        ]
    }, {
        path: "/login",
        name: "Login",
        meta: {
            title: '??????'
        },
        component: () => import (
        /* webpackChunkName: "login" */
        "../views/Login.vue")
    }
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
});

router.beforeEach((to, from, next) => {
    document.title = `${to.meta.title} | Resource Manage System`;
    const role = localStorage.getItem('ms_username');
    if (!role && to.path !== '/login') {
        next('/login');
    } else if (to.meta.permission) {
        // ???????????????????????????????????????????????????????????????????????????????????????
        role === 'admin'
            ? next()
            : next('/403');
    } else {
        next();
    }
});

export default router;