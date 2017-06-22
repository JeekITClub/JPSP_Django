/**
 * Created by wto on 2017/5/12 0012.
 */
import Vue from 'vue'
import Router from 'vue-router'
import PostList from '../pages/admin_cd/PostList.vue'
import ActivityList from '../pages/admin_cd/ActivityList.vue'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'post',
      component: PostList
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
    }
  ]
})
