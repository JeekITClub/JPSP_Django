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
import FileUpload from '../pages/admin_cd/FileUpload.vue'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: Dashboard
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/activity',
      name: 'Activity',
      component: ActivityList
    },
    {
      path: '/post',
      name: 'Post',
      component: PostList
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
    },
    {
      path: '/club',
      name: 'ClubList',
      component: ClubList
    },
    {
      path: '/file/upload',
      name: 'FileUpload',
      component: FileUpload
    }
  ]
})
