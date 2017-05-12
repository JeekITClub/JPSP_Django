/**
 * Created by wto on 2017/5/12 0012.
 */
import Vue from 'vue'
import Router from 'vue-router'
import index from '@/pages/admin_cd/index'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: index
    },
    {
      path:'/login',
      name:'login',
      component: login
    },
    {
      path:'/post/overview',
      name:'post_overview',
      component: post_overview
    },
    {
      path:'/post/edit',
      name:'post_edit',
      component: post_edit
    },
    {
      path:'/post/verify',
      name:'log',
      component: login
    },
    {
      path:'/login',
      name:'login',
      component: login
    },
    {
      path:'/login',
      name:'login',
      component: login
    },
    {
      path:'/login',
      name:'login',
      component: login
    },
    {
      path:'/login',
      name:'login',
      component: login
    },
    {
      path:'/login',
      name:'login',
      component: login
    },
    {
      path:'/login',
      name:'login',
      component: login
    },
    {
      path:'/login',
      name:'login',
      component: login
    },
    {
      path:'/login',
      name:'login',
      component: login
    },
    {
      path:'/login',
      name:'login',
      component: login
    },
    {
      path:'/login',
      name:'login',
      component: login
    },
    {
      path:'/login',
      name:'login',
      component: login
    },
    {
      path:'/login',
      name:'login',
      component: login
    },
    {
      path:'/login',
      name:'login',
      component: login
    },
    {
      path:'/login',
      name:'login',
      component: login
    },


  ]
})
