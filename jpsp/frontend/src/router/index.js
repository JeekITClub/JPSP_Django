import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)
import Index from '@/pages/index/index.vue'
import Login from '@/pages/index/Login.vue'
import ClubIndex from '@/pages/index/ClubIndex'
import ProfileEdit from '@/pages/index/ProfileEdit.vue'
import ActivityList from '../pages/index/ActiviytList.vue'
import ClubShow from '@/pages/index/ClubShow.vue'
import EventList from '../pages/index/EventList.vue'
import Contact from '@/pages/public/Contact.vue'
import About from '@/pages/public/About.vue'
import EstablishClub from '@/pages/index/EstablishClub.vue'
// import LostAndFound from '../pages/index/LostAndFound.vue'
export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: Index
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/club/:ClubId',
      name: 'ClubIndex',
      component: ClubIndex
    },
    {
      path: '/activity',
      name: 'ActivityList',
      component: ActivityList
    },
    {
      path: '/profile',
      name: 'ProfileEdit',
      component: ProfileEdit
    },
    {
      path: '/club/establish',
      name: 'EstablishClub',
      component: EstablishClub
    },
    {
      path: '/club',
      name: 'ClubShow',
      component: ClubShow
    },
    {
      path: '/event/list',
      name: 'EventList',
      component: EventList
    },
    {
      path: '/contact',
      name: 'Contact',
      component: Contact
    },
    {
      path: '/about',
      name: 'About',
      component: About
    }
  ]
})
