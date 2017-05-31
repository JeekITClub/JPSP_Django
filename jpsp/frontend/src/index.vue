<template>
  <div id="app">
  <JNavTop></JNavTop>
    <router-view></router-view>
  <JFooter></JFooter>
  </div>
</template>

<script>
import JNavTop from './components/public/JNavTop.vue'
import JFooter from './components/public/JFooter.vue'

export default {
  name: 'app',
  components: {
    JNavTop,
    JFooter
  }
}
</script>

<style>
</style>
