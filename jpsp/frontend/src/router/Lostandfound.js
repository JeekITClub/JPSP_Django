/**
 * Created by TT on 2017/6/8.
 */
import Vue from 'vue'
import Router from 'vue-router'
import index from '../pages/index/index.vue
import Lostandfound from '../../components/index/Lostandfound.vue'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: index
    },
    {
      path: '/Lostandfound',
      name: 'Lostandfound',
      component: Lostandfound
    }
  ]
})
