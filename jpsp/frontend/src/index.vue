<template>
  <div id="app">
  <NavTop></NavTop>
    <router-view></router-view>
  </div>
</template>

<script>
import NavTop from './components/public/NavTop.vue'

export default {
  name: 'app',
  components: {
    NavTop
  }
}
</script>

<style>
</style>
