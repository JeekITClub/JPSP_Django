import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)
// import ActivityList from '../pages/index/ActiviytList.vue'
// import EventList from '../pages/index/EventList.vue'
// import LostAndFound from '../pages/index/LostAndFound.vue'
export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: resolve => require(['@/pages/index/index.vue'], resolve)
    },
    {
      path: '/login',
      name: 'login',
      component: resolve => require(['@/pages/index/Login.vue'], resolve)
    },
    {
      path: '/club/:ClubId',
      name: 'ClubIndex',
      component: resolve => require(['@/pages/index/ClubIndex.vue'], resolve)
    },
    {
      path: '/activity/list',
      name: 'ActivityList',
      component: resolve => require(['@/components/public/Future.vue'], resolve)
    },
    {
      path: '/activity/news',
      name: 'ActivityNews',
      component: resolve => require(['@/components/public/Future.vue'], resolve)
    },
    {
      path: '/profile',
      name: 'ProfileEdit',
      component: resolve => require(['@/pages/index/ProfileEdit.vue'], resolve)
    },
    {
      path: '/club',
      name: 'ClubShow',
      component: resolve => require(['@/pages/index/ClubShow.vue'], resolve)
    },
    {
      path: '/event/list',
      name: 'EventList',
      component: resolve => require(['@/components/public/Future.vue'], resolve)
    },
    {
      path: '/contact',
      name: 'Contact',
      component: resolve => require(['@/components/public/Contact.vue'], resolve)
    },
    {
      path: '/about',
      name: 'About',
      component: resolve => require(['@/components/public/About.vue'], resolve)
    },
    {
      path: '/lost',
      name: 'LostAndFound',
      component: resolve => require(['@/components/public/Future.vue'], resolve)
    },
    {
      path: '/basic',
      name: 'Basic',
      component: resolve => require(['@/components/index/UserProfile.vue'], resolve)
    },
    {
      path: '/changepw',
      name: 'ChangePw',
      component: resolve => require(['@/components/index/ChangePassword.vue'], resolve)
    },
    {
      path: '/clubattended',
      name: 'ClubAttended',
      component: resolve => require(['@/components/index/ClubAttended.vue'], resolve)
    },
    {
      path: '/activityenrolled',
      name: 'ActivityEnrolled',
      component: resolve => require(['@/components/public/Future.vue'], resolve)
    },
    {
      path: '/activityattended',
      name: 'ActivityAttended',
      component: resolve => require(['@/components/public/Future.vue'], resolve)
    },
    {
      path: '/establish',
      name: 'EstablishClub',
      component: resolve => require(['@/components/index/Establish.vue'], resolve)
    }
  ]
})
