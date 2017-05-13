// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import admin_club from './admin_club'
import router from './router/admin_club.js'
import ElementUI from 'element-ui'
Vue.config.productionTip = false

Vue.use(ElementUI)

/* eslint-disable no-new */

new Vue({
  el: '#app_admin_club',
  router,
  template: '<admin_club/>',
  components: { admin_club },
  render: h => h(admin_club)
})
