import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/pages/admin_club/Login'
import PostEdit from '@/pages/admin_club/PostEdit'
import ProfileEdit from '@/pages/admin_club/ProfileEdit'
import ClubPageSettings from '@/pages/admin_club/ClubPageSettings'
import MemberManagement from '@/pages/admin_club/MemberManagement'
import RecruitClassroomEdit from '@/pages/admin_club/RecruitClassroomEdit'
import RecruitClassroomList from '@/pages/admin_club/RecruitClassroomList.vue'
import About from '@/pages/public/About.vue'
import Contact from '@/pages/public/Contact.vue'
import Establish from '@/pages/admin_club/Establish.vue'
import ActivityApply from '@/pages/admin_club/ActivityApply.vue'
import ActivityList from '@/pages/admin_club/ActivityList.vue'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: Login
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/post',
      name: 'Post',
      component: PostEdit
    },
    {
      path: '/profile',
      name: 'Profile',
      component: ProfileEdit
    },
    {
      path: '/establish',
      name: 'Establish',
      component: Establish
    },
    {
      path: '/page',
      name: 'ClubPageSettings',
      component: ClubPageSettings
    },
    {
      path: '/activity/apply',
      name: 'ActivityApply',
      component: ActivityApply
    },
    {
      path: '/activity/list',
      name: 'ActivityList',
      component: ActivityList
    },
    {
      path: '/recruit/classroom/apply',
      name: 'RecruitClassroom',
      component: RecruitClassroomEdit
    },
    {
      path: '/recruit/classroom/list',
      name: 'RecruitClassroomList',
      component: RecruitClassroomList
    },
    {
      path: '/member',
      name: 'Member',
      component: MemberManagement
    },
    {
      path: '/about',
      name: 'About',
      component: About
    },
    {
      path: '/contact',
      name: 'Contact',
      component: Contact
    }
  ]
})
