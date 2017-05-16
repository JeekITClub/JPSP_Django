import Vue from 'vue'
import Router from 'vue-router'
import index from '@/pages/index/index'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: ProfileEdit
    },
    {
      path: '/post',
      name: 'Post',
      component: PostEdit
    }
  ]
})
