<template>
  <div id="app_club">
    <div>
        <JNavTop></JNavTop>
      <div class="container">
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<script>
  import JNavTop from '../src/components/admin_club/JNavTop.vue'
  export default {
    components: {
      'JNavTop': JNavTop
    },
    name: 'app_club'
  }
</script>

<style>
   #app_club .container {
     margin-right: auto;
     margin-left: auto;
     width: 100%;
  }
</style>
