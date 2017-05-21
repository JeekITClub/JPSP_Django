import Vue from 'vue'
import Router from 'vue-router'
// import index from '@/pages/index/index'
Vue.use(Router)
import NavTop from '@/components/admin_club/NavTop.vue'

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: NavTop
    }
  ]
})
