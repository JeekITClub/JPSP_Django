import Vue from 'vue'
import Router from 'vue-router'
// import RecruitClassroomForm from '@/pages/admin_club/RecruitClassroomForm.vue'
// import RecruitClassroomList from '@/pages/admin_club/RecruitClassroomList.vue'
// import ActivityForm from '@/pages/admin_club/ActivityForm.vue'
// import ActivityList from '@/pages/admin_club/ActivityList.vue'
// import EventForm from '@/pages/admin_club/EventForm.vue'
// import EventList from '@/pages/admin_club/EventList.vue'
// import FileDownload from '@/pages/admin_club/FileDownload.vue'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: resolve => require(['@/pages/admin_club/Login'], resolve)
    },
    {
      path: '/dashboard',
      name: 'Dashboard',
      component: resolve => require(['@/pages/admin_club/DashBoard.vue'], resolve)
    },
    {
      path: '/login',
      name: 'Login',
      component: resolve => require(['@/pages/admin_club/Login'], resolve)
    },
    {
      path: '/post/form',
      name: 'PostForm',
      component: resolve => require(['@/pages/admin_club/PostForm.vue'], resolve)
    },
    {
      path: '/post/list',
      name: 'PostList',
      component: resolve => require(['@/pages/admin_club/PostList.vue'], resolve)
    },
    {
      path: '/profile',
      name: 'Profile',
      component: resolve => require(['@/pages/admin_club/ProfileEdit'], resolve)
    },
    {
      path: '/page',
      name: 'ClubPageSettings',
      component: resolve => require(['@/pages/admin_club/ClubPageSettings'], resolve)
    },
    {
      path: '/activity/form',
      name: 'ActivityForm',
      component: resolve => require(['@/components/public/Future.vue'], resolve)
    },
    {
      path: '/activity/list',
      name: 'ActivityList',
      component: resolve => require(['@/components/public/Future.vue'], resolve)
    },
    {
      path: '/recruit/classroom/apply',
      name: 'RecruitClassroom',
      component: resolve => require(['@/components/public/Future.vue'], resolve)
    },
    {
      path: '/recruit/classroom/list',
      name: 'RecruitClassroomList',
      component: resolve => require(['@/components/public/Future.vue'], resolve)
    },
    {
      path: '/member',
      name: 'Member',
      component: resolve => require(['@/pages/admin_club/MemberManagement'], resolve)
    },
    {
      path: '/about',
      name: 'About',
      component: resolve => require(['@/components/public/About.vue'], resolve)
    },
    {
      path: '/contact',
      name: 'Contact',
      component: resolve => require(['@/components/public/Contact.vue'], resolve)
    },
    {
      path: '/activity/record',
      name: 'ActivityRecord',
      component: resolve => require(['@/components/public/Future.vue'], resolve)
    },
    {
      path: '/event/list',
      name: 'EventList',
      component: resolve => require(['@/components/public/Future.vue'], resolve)
    },
    {
      path: '/password',
      name: 'ChangePassword',
      component: resolve => require(['@/pages/admin_club/ChangePassword.vue'], resolve)
    },
    {
      path: '/file/upload',
      name: 'FileUpload',
      component: resolve => require(['@/pages/admin_club/FileUpload.vue'], resolve)
    },
    {
      path: '/file/download',
      name: 'FileDownload',
      component: resolve => require(['@/components/public/Future.vue'], resolve)
    }
  ]
})
