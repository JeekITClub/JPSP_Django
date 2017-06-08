<template>
  <div id="app_cd">
    <div>
      <j-nav-top></j-nav-top>
    </div>
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
