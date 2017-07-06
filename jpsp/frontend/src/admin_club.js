// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import AdminClub from './AdminClub.vue'
import router from './router/admin_club.js'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-default/index.css'
import 'bootstrap/dist/css/bootstrap.css'
import Vuex from 'vuex'
import axios from 'axios'
Vue.config.productionTip = false
Vue.prototype.$ajax = axios
Vue.use(ElementUI)
Vue.use(Vuex)
/* eslint-disable no-new */

const AdminClubVuexStore = new Vuex.Store({
  state: {
    ClubId: '',
    UserName: '',
    Token: '',
    Authenticated: null
  },
  mutations: {
    Authenticated (state, If) {
      state.Authenticated = If
    },
    ApplyUserName (state, UserName) {
      state.UserName = UserName
    },
    ApplyToken (state, Token) {
      state.Token = Token
    },
    ApplyClubId (state, ClubId) {
      state.ClubId = ClubId
    }
  }
})

new Vue({
  el: '#app_club',
  router,
  store: AdminClubVuexStore,
  template: '<App/>',
  components: {AdminClub},
  render: h => h(AdminClub)
})
