// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import AdminClub from './AdminClub.vue'
import router from './router/admin_club.js'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-default/index.css'
import 'bootstrap/dist/css/bootstrap.css'
import Vuex from 'vuex'
Vue.config.productionTip = false

Vue.use(ElementUI)
Vue.use(Vuex)
/* eslint-disable no-new */

const AdminClubVuexStore = new Vuex.Store({
  state: {
    ClubId: '',
    CludName: '',
    Token: '',
    Login_in: false
  },
  mutations: {
    Login_in (state) {
      state.Login_in = true
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
