import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)
export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: resolve => require(['@/pages/index/Index.vue'], resolve)
    },
    {
      path: '/Login',
      name: 'login',
      component: resolve => require(['@/pages/index/Login.vue'], resolve)
    },
    {
      path: '/Club/:ClubId',
      name: 'ClubPage',
      component: resolve => require(['@/pages/index/ClubPage.vue'], resolve)
    },
    // {
    //   path: '/activity/list',
    //   name: 'ActivityList',
    //   component: resolve => require(['@/components/public/Future.vue'], resolve)
    // },
    // {
    //   path: '/Activity/news',
    //   name: 'ActivityNews',
    //   component: resolve => require(['@/components/public/Future.vue'], resolve)
    // },
    {
      path: '/User/Dashboard',
      name: 'Dashboard',
      component: resolve => require(['@/pages/index/Dashboard.vue'], resolve)
    },
    {
      path: '/Club',
      name: 'ClubShow',
      component: resolve => require(['@/pages/index/ClubShow.vue'], resolve)
    },
    // {
    //   path: '/event/list',
    //   name: 'EventList',
    //   component: resolve => require(['@/components/public/Future.vue'], resolve)
    // },
    {
      path: '/Contact',
      name: 'Contact',
      component: resolve => require(['@/components/public/Contact.vue'], resolve)
    },
    {
      path: '/About',
      name: 'About',
      component: resolve => require(['@/components/public/About.vue'], resolve)
    },
    {
      path: '/LAF',
      name: 'LostAndFound',
      component: resolve => require(['@/components/public/Future.vue'], resolve)
    },
    {
      path: '/User/Profile',
      name: 'ProfileEdit',
      component: resolve => require(['@/pages/index/ProfileEdit.vue'], resolve)
    },
    {
      path: '/User/Password',
      name: 'Password',
      component: resolve => require(['@/components/index/ChangePassword.vue'], resolve)
    },
    {
      path: '/User/Club',
      name: 'ClubAttended',
      component: resolve => require(['@/components/index/ClubAttended.vue'], resolve)
    },
    // {
    //   path: '/User/Activity',
    //   name: 'ActivityEnrolled',
    //   component: resolve => require(['@/components/public/Future.vue'], resolve)
    // },
    // {
    //   path: '/User/Activity',
    //   name: 'ActivityAttended',
    //   component: resolve => require(['@/components/public/Future.vue'], resolve)
    // },
    {
      path: '/Establish',
      name: 'EstablishClub',
      component: resolve => require(['@/components/index/Establish.vue'], resolve)
    }
  ]
})
