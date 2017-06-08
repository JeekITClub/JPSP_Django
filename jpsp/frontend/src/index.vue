<template>
  <div id="app">
  <JNavTop></JNavTop>
    <router-view></router-view>
  <JFooter></JFooter>
  </div>
</template>

<script>
import JNavTop from './components/index/JNavTop.vue'
import JFooter from './components/index/JFooter.vue'
import Lostandfound from './components/index/Lostandfound.vue'

export default {
  name: 'app',
  components: {
    JNavTop,
    JFooter,
    Lostandfound
  }
}
</script>

<style>
</style>
