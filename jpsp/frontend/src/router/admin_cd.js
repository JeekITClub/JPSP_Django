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
      path: '/login',
      name: 'Login',
      component: resolve => require(['@/pages/admin_cd/Login'], resolve)
    },
    {
      path: '/activity',
      name: 'Activity',
      component: resolve => require(['@/pages/admin_cd/ActivityList'], resolve)
    },
    {
      path: '/post',
      name: 'Post',
      component: resolve => require(['../pages/admin_cd/PostList.vue'], resolve)
    },
    {
      path: '/contact',
      name: 'Contact',
      component: resolve => require(['../pages/public/Contact.vue'], resolve)
    },
    {
      path: '/about',
      name: 'About',
      component: resolve => require(['../pages/public/About.vue'], resolve)
    },
    {
      path: '/club',
      name: 'ClubList',
      component: resolve => require(['../pages/admin_cd/ClubList.vue'], resolve)
    },
    {
      path: '/file/upload',
      name: 'FileUpload',
      component: resolve => require(['../pages/admin_cd/FileUpload.vue'], resolve)
    },
    {
      path: '/user/one',
      name: 'UserOne',
      component: resolve => require(['../components/admin_cd/UserOne.vue'], resolve)
    },
    {
      path: '/user',
      name: 'User',
      component: resolve => require(['../components/admin_cd/User.vue'], resolve)
    }
  ]
})
