// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import index from './index.vue'
import router from './router/index.js'
import {Pagination, Notification, Icon} from 'element-ui'
import Vuex from 'vuex'
import axios from 'axios'
import './assets/index/css/bulma.css'
import '../static/icon.css'
import '../static/notification.css'
var VueCookie = require('vue-cookie')
Vue.config.productionTip = false
Vue.prototype.$ajax = axios
Vue.use(Vuex)
Vue.use(Pagination)
Vue.use(Icon)
Vue.use(VueCookie)
Vue.prototype.$notify = Notification
/* eslint-disable no-new */
const UserVuexStore = new Vuex.Store({
  state: {
    Api: 'http://127.0.0.1:3000/'
  }
//     UserId: '用户名',
//     UserName: '',
//     Token: '',
//     Authenticated: null
//   mutations: {
//     Authenticated (state, If) {
//       state.Authenticated = If
//     },
//     ApplyUserName (state, UserName) {
//       state.UserName = UserName
//     },
//     ApplyToken (state, Token) {
//       state.Token = Token
//     },
//     ApplyUserId (state, UserId) {
//       state.UserId = UserId
//     }
//   }
})

new Vue({
  el: '#app',
  router,
  store: UserVuexStore,
  template: '<App/>',
  components: {index},
  render: h => h(index)
})
