import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/pages/admin_club/Login'
import ProfileEdit from '@/pages/admin_club/ProfileEdit'
import ClubPageSettings from '@/pages/admin_club/ClubPageSettings'
import MemberManagement from '@/pages/admin_club/MemberManagement'
import RecruitClassroomForm from '@/pages/admin_club/RecruitClassroomForm.vue'
import RecruitClassroomList from '@/pages/admin_club/RecruitClassroomList.vue'
import About from '@/pages/public/About.vue'
import Contact from '@/pages/public/Contact.vue'
import ActivityForm from '@/pages/admin_club/ActivityForm.vue'
import ActivityList from '@/pages/admin_club/ActivityList.vue'
import EventForm from '@/pages/admin_club/EventForm.vue'
import EventList from '@/pages/admin_club/EventList.vue'
import PostForm from '@/pages/admin_club/PostForm.vue'
import PostList from '@/pages/admin_club/PostList.vue'
import DashBoard from '@/pages/admin_club/DashBoard.vue'
import ChangePassword from '@/pages/admin_club/ChangePassword.vue'
import FileUpload from '@/pages/admin_club/FileUpload.vue'
import FileDownload from '@/pages/admin_club/FileDownload.vue'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: Login
    },
    {
      path: '/dashboard',
      name: 'Dashboard',
      component: DashBoard
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/post/form',
      name: 'PostForm',
      component: PostForm
    },
    {
      path: '/post/list',
      name: 'PostList',
      component: PostList
    },
    {
      path: '/profile',
      name: 'Profile',
      component: ProfileEdit
    },
    {
      path: '/page',
      name: 'ClubPageSettings',
      component: ClubPageSettings
    },
    {
      path: '/activity/form',
      name: 'ActivityForm',
      component: ActivityForm
    },
    {
      path: '/activity/list',
      name: 'ActivityList',
      component: ActivityList
    },
    {
      path: '/recruit/classroom/apply',
      name: 'RecruitClassroom',
      component: RecruitClassroomForm
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
    },
    {
      path: '/event/form',
      name: 'EventForm',
      component: EventForm
    },
    {
      path: '/event/list',
      name: 'EventList',
      component: EventList
    },
    {
      path: '/password',
      name: 'ChangePassword',
      component: ChangePassword
    },
    {
      path: '/file/upload',
      name: 'FileUpload',
      component: FileUpload
    },
    {
      path: '/file/download',
      name: 'FileDownload',
      component: FileDownload
    }
  ]
})
