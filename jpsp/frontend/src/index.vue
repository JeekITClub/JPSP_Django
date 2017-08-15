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
  export default {
    name: 'app',
    components: {
      JNavTop,
      JFooter
    }
  }
</script>

<style>
  @import 'assets/element-ui/index.css';
</style>
