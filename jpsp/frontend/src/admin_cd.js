// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import AdminCD from './AdminCD.vue'
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-default/index.css'
import Vuex from 'vuex'
import 'bootstrap/dist/css/bootstrap.css'
Vue.config.productionTip = false
Vue.use(ElementUI)
Vue.use(Vuex)
/* eslint-disable no-new */

const AdminCDVuexStore = new Vuex.Store({
  state: {
    UserName: '用户名',
    Token: '',
    Authenticated: false
  },
  mutations: {
    Authenticate (state) {
      state.Authenticated = true
    },
    ApplyUserName (state, UserName) {
      state.UserName = UserName
    },
    ApplyToken (state, Token) {
      state.Token = Token
    }
  }
})

new Vue({
  el: '#app_cd',
  router,
  store: AdminCDVuexStore,
  template: '<App/>',
  components: {AdminCD},
  render: h => h(AdminCD)
})
