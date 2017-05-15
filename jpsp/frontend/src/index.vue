<template>
  <div id="app">
  <NavTop></NavTop>
    <router-view></router-view>
  <JFooter></JFooter>
  </div>
</template>

<script>
import NavTop from './components/public/NavTop.vue'
import JFooter from './components/public/JFooter.vue'

export default {
  name: 'app',
  components: {
    NavTop,
    JFooter
  }
}
</script>

<style>
</style>
