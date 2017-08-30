// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import AdminCD from './AdminCD.vue'
import router from './router/admin_cd'
import {
  Pagination,
  Table,
  TableColumn,
  DatePicker,
  TimePicker,
  Notification,
  Tabs,
  TabPane,
  FormItem,
  Form
} from 'element-ui'
import './assets/index/css/bulma.css'
import Vuex from 'vuex'
import axios from 'axios'
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
Vue.use(VueCookie)
Vue.prototype.$notify = Notification
// Vue.use(Vuex)
/* eslint-disable no-new */

const AdminCDVuexStore = new Vuex.Store({
  state: {
    Api: 'http://127.0.0.1:8000/api/'
  }
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
})

new Vue({
  el: '#app_cd',
  router,
  store: AdminCDVuexStore,
  template: '<App/>',
  components: {AdminCD},
  render: h => h(AdminCD)
  // created () {
  //   this.checkLogin()
  // },
  // watch: {
  //   '$route': 'checkLogin'
  // },
  // methods: {
  //   checkLogin () {
  //     if (this.$cookie.get('CDAuthentiacated') !== true) {
  //       this.$router.push('/login')
  //     }
  //   }
  // }
})
