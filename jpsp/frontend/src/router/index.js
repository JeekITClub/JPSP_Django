import Vue from 'vue'
import Router from 'vue-router'
// import index from '@/pages/index/index'
import PostEdit from '@/pages/admin_club/PostEdit.vue'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: PostEdit
    },
    {
      path: '/post',
      name: 'post',
      component: PostEdit
    }
  ]
})
