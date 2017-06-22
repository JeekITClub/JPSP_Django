<template>
  <div id="app_cd">
    <JNavTop></JNavTop>
    <router-view></router-view>
  </div>
</template>

<script>
  import JNavTop from '@/components/admin_cd/JNavTop.vue'
  export default {
    components: {
      'JNavTop': JNavTop
    },
    name: 'app_cd'
  }
</script>

<style>
</style>
