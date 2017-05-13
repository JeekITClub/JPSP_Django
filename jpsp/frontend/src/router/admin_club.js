/**
 * Created by wto on 2017/5/12 0012.
 */
import Vue from 'vue'
import Router from 'vue-router'
import index from '@/pages/admin_club/index.vue'
import dashboard from '@/pages/admin_club/dashboard.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: index
    },
    {
      path: '/',
      name: 'dashboard',
      component: dashboard
    }
  ]
})
