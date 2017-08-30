<template>
  <div id="app">
    <JNavTop></JNavTop>
    <div class="columns" v-if="GetIndexAuthenticated === 'true' && this.$route.name === 'ProfileEdit'">
      <div class="column is-2">
        <JAside></JAside>
      </div>
      <div class="column index-content">
        <router-view></router-view>
      </div>
    </div>
    <div v-else>
      <router-view></router-view>
    </div>
    <JFooter></JFooter>
  </div>
</template>

<script>
  import JNavTop from './components/index/JNavTop.vue'
  import JFooter from './components/index/JFooter.vue'
  import JAside from './components/index/JAside.vue'

  export default {
    name: 'app',
    components: {
      JNavTop,
      JFooter,
      JAside
    },
    computed: {
      GetIndexAuthenticated () {
        return this.$cookie.get('IndexAuthenticated')
      }
    }
  }
</script>

<style scoped>
  .index-content {
    padding-bottom: 0;
    padding-left: 0;
  }
</style>
