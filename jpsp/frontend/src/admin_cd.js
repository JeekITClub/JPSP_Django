// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import AdminCD from './AdminCD.vue'
import router from './router/admin_cd'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-default/index.css'
// import Vuex from 'vuex'
import 'bootstrap/dist/css/bootstrap.css'
import axios from 'axios'
Vue.config.productionTip = false
Vue.prototype.$ajax = axios
Vue.config.productionTip = false
Vue.use(ElementUI)
import { getCookie } from 'tiny-cookie'
// Vue.use(Vuex)
/* eslint-disable no-new */

// const AdminCDVuexStore = new Vuex.Store({
//   state: {
//     UserName: '用户名',
//     UserId: '',
//     Token: '',
//     Authenticated: null
//   },
//   mutations: {
//     Authenticate (state, If) {
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
// })

new Vue({
  el: '#app_cd',
  router,
  // store: AdminCDVuexStore,
  template: '<App/>',
  components: {AdminCD},
  render: h => h(AdminCD),
  created () {
    this.checkLogin()
  },
  watch: {
    '$route': 'checkLogin'
  },
  methods: {
    checkLogin () {
      if (getCookie('CDAuthentiacated') === true) {
        this.$router.push('/dashboard')
      } else {
        this.$router.push('/login')
      }
    }
  }
})
