/**
 * Created by wto on 2017/5/12 0012.
 */
import Vue from 'vue'
import Router from 'vue-router'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: resolve => require(['../pages/admin_cd/Dashboard.vue'], resolve)
    },
    {
      path: '/Login',
      name: 'Login',
      component: resolve => require(['@/pages/admin_cd/Login'], resolve)
    },
    {
      path: '/Activity',
      name: 'Activity',
      component: resolve => require(['@/components/public/Future'], resolve)
    },
    {
      path: '/Post',
      name: 'Post',
      component: resolve => require(['../pages/admin_cd/PostList.vue'], resolve)
    },
    {
      path: '/Contact',
      name: 'Contact',
      component: resolve => require(['../pages/public/Contact.vue'], resolve)
    },
    {
      path: '/About',
      name: 'About',
      component: resolve => require(['../pages/public/About.vue'], resolve)
    },
    {
      path: '/Club',
      name: 'ClubList',
      component: resolve => require(['../pages/admin_cd/ClubList.vue'], resolve)
    },
    {
      path: '/File/Upload',
      name: 'FileUpload',
      component: resolve => require(['../components/public/Future.vue'], resolve)
    },
    {
      path: '/File/Download',
      name: 'FileDownload',
      component: resolve => require(['../components/public/Future.vue'], resolve)
    },
    {
      path: '/User/One',
      name: 'UserOne',
      component: resolve => require(['../pages/admin_cd/UserOne.vue'], resolve)
    },
    {
      path: '/User',
      name: 'User',
      component: resolve => require(['../pages/admin_cd/User.vue'], resolve)
    }
  ]
})
