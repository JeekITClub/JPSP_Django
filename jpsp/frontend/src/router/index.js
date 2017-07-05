import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)
import index from '@/pages/index/index.vue'
import Login from '@/pages/index/Login.vue'
import ClubIndex from '@/pages/index/ClubIndex'
import ProfileEdit from '@/pages/index/ProfileEdit.vue'
import ActivityList from '../pages/index/ActiviytList.vue'
import ClubList from '@/pages/index/ClubList.vue'
// import LostAndFound from '../pages/index/LostAndFound.vue'
export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: index
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
      path: '/club',
      name: 'ClubList',
      component: ClubList
    }
  ]
})
