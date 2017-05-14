// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import AdminCD from './AdminCD.vue'
import router from './router'

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app_cd',
  router,
  template: '<App/>',
  components: { AdminCD },
  render: h => h(AdminCD)
})
