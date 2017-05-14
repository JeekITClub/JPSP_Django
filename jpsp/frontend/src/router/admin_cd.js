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
      name:'post_verify',
      component: post_verify
    },
    {
      path:'/post/denied',
      name:'post_denied',
      component: post_denied
    },
    {
      path:'/post/analysis',
      name:'post_analysis',
      component: post_analysis
    },
    {
      path:'/club/',
      name:'club',
      component: club_list
    },
    {
      path:'/club/delete',
      name:'club_delete',
      component: club_delete
    },
    {
      path:'/club/verify',
      name:'club_verify',
      component: club_verify
    },
    {
      path:'/club/profile',
      name:'club_profile',
      component: club_profile
    },
    // {
    //   path:'/login',
    //   name:'login',
    //   component: login
    // },
    // {
    //   path:'/login',
    //   name:'login',
    //   component: login
    // },
    // {
    //   path:'/login',
    //   name:'login',
    //   component: login
    // },
    // {
    //   path:'/login',
    //   name:'login',
    //   component: login
    // },
    // {
    //   path:'/login',
    //   name:'login',
    //   component: login
    // },
    // {
    //   path:'/login',
    //   name:'login',
    //   component: login
    // },
    // {
    //   path:'/login',
    //   name:'login',
    //   component: login
    // },
    // {
    //   path:'/login',
    //   name:'login',
    //   component: login
    // },


  ]
})
