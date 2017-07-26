/**
 * Created by wto on 2017/5/12 0012.
 */
import Vue from 'vue'
import Router from 'vue-router'
import Login from '../pages/admin_cd/Login.vue'
import PostList from '../pages/admin_cd/PostList.vue'
import ActivityList from '../pages/admin_cd/ActivityList.vue'
import Contact from '../pages/public/Contact.vue'
import About from '../pages/public/About.vue'
import ClubList from '../pages/admin_cd/ClubList.vue'
import Dashboard from '../pages/admin_cd/Dashboard.vue'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: Dashboard
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/activity',
      name: 'activity',
      component: ActivityList
    },
    {
      path: '/post',
      name: 'post',
      component: PostList
    },
    {
      path: '/contact',
      name: 'contact',
      component: Contact
    },
    {
      path: '/about',
      name: 'about',
      component: About
    },
    {
      path: '/club',
      name: 'club',
      component: ClubList
    }
  ]
})
