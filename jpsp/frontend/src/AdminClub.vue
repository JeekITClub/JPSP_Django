<template>
  <div id="app_club">
    <JNavTop></JNavTop>
    <div class="container">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
  import ClubAside from '@/components/admin_club/ClubAside.vue'
  import JNavTop from '@/components/admin_club/JNavTop.vue'
  export default {
    components: {
      'ClubAside': ClubAside,
      'JNavTop': JNavTop
    },
    computed: {
      Authenticate () {
        return this.$store.state.Authenticated
      }
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
