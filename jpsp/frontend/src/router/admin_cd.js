/**
 * Created by wto on 2017/5/12 0012.
 */
import Vue from 'vue'
import Router from 'vue-router'
import Index from '../pages/admin_cd/index.vue'
import PostList from '../pages/admin_cd/PostList.vue'
import ActivityList from '../pages/admin_cd/ActivityList.vue'
import Contact from '../pages/public/Contact.vue'
import About from '../pages/public/About.vue'
import ClubList from '../pages/admin_cd/ClubList.vue'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: Index
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
