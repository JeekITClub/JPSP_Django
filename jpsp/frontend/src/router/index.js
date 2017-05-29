import Vue from 'vue'
import Router from 'vue-router'
// import index from '@/pages/index/index'
Vue.use(Router)

import index from '../pages/index/index.vue'
import PostEdit from '../pages/admin_club/PostEdit.vue'
export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: index
    },
    {
      path: '/post',
      name: 'Post',
      component: PostEdit
    }
  ]
})
