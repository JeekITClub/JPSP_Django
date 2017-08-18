// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import AdminClub from './AdminClub.vue'
import router from './router/admin_club.js'
import { Pagination, Table, TableColumn, DatePicker, TimePicker, Notification, Tabs, TabPane, FormItem, Form } from 'element-ui'
import './assets/index/css/bulma.css'
import Vuex from 'vuex'
import axios from 'axios'
import VueQuillEditor from 'vue-quill-editor'
var VueCookie = require('vue-cookie')
Vue.config.productionTip = false
Vue.prototype.$ajax = axios
Vue.use(Pagination)
Vue.use(TableColumn)
Vue.use(Table)
Vue.use(DatePicker)
Vue.use(TimePicker)
Vue.use(Tabs)
Vue.use(Form)
Vue.use(FormItem)
Vue.use(TabPane)
Vue.use(Vuex)
Vue.use(VueQuillEditor)
Vue.use(VueCookie)
Vue.prototype.$notify = Notification
/* eslint-disable no-new */
const AdminClubVuexStore = new Vuex.Store({
  state: {
    API: 'http://127.0.0.1:8080/api/'
  }
  // mutations: {
  //   Authenticated (state, If) {
  //     state.Authenticated = If
  //   },
  //   ApplyUserName (state, UserName) {
  //     state.UserName = UserName
  //   },
  //   ApplyToken (state, Token) {
  //     state.Token = Token
  //   },
  //   ApplyClubId (state, ClubId) {
  //     state.ClubId = ClubId
  //   }
  // }
})

new Vue({
  el: '#app_club',
  router,
  store: AdminClubVuexStore,
  template: '<App/>',
  components: {AdminClub},
  render: h => h(AdminClub),
  // created () {
  //   this.checkLogin()
  // },
  // watch: {
  //   '$route': 'checkLogin'
  // },
  // TODO: 最后上面的要取消注释
  methods: {
    checkLogin () {
      if (this.$cookie.get('ClubAuthenticated') === true) {
        this.$router.push('/dashboard')
      } else {
        this.$router.push('/login')
      }
    }
  }
})
