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
import LostAndFound from './components/index/LostAndFound.vue'
export default {
  name: 'app',
  components: {
    JNavTop,
    JFooter,
    LostAndFound
  }
}
</script>

<style>
</style>
