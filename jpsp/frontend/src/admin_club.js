// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import AdminClub from './AdminClub.vue'
import router from './router/admin_club.js'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-default/index.css'
import Vuex from 'vuex'
Vue.config.productionTip = false

Vue.use(ElementUI)
Vue.use(Vuex)
/* eslint-disable no-new */
const admin_club_vuex_store = new Vuex.Store({
  state: {
    ClubId: "",
    CludName: "",
    Token: ""
  },
  mutations: {
    login(state){
      alert(state.user_name);
    }
  }
})

new Vue({
  el: '#app_club',
  router,
  store: admin_club_vuex_store,
  template: '<App/>',
  components: {AdminClub},
  render: h => h(AdminClub)
})
