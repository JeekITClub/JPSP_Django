import Vue from 'vue'
import Router from 'vue-router'
// import index from '@/pages/index/index'
import PostEdit from '@/pages/admin_club/PostEdit.vue'
import ProfileEdit from '@/pages/admin_club/ProfileEdit.vue'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: ProfileEdit
    },
    {
      path: '/post',
      name: 'post',
      component: PostEdit
    }
  ]
})
