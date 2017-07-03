import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)
import index from '@/pages/index/index.vue'
import Login from '@/pages/index/Login.vue'
import ClubIndex from '@/pages/index/ClubIndex'
import ClubPost from '@/pages/index/ClubPost.vue'
import ClubPostList from '@/pages/index/ClubPostList.vue'
import ProfileEdit from '@/pages/index/ProfileEdit.vue'
import ActivityList from '../pages/index/ActiviytList.vue'
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
      path: '/clubindex',
      name: 'ClubIndex',
      component: ClubIndex
    },
    {
      path: '/clubpostlist',
      name: 'ClubPostList',
      component: ClubPostList
    },
    {
      path: '/clubpost',
      name: 'ClubPost',
      component: ClubPost
    },
    {
      path: '/alist',
      name: 'ActivityList',
      component: ActivityList
    },
    {
      path: '/profile',
      name: 'ProfileEdit',
      component: ProfileEdit
    }
  ]
})
