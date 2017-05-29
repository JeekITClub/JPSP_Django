<template>
  <div id="app_club">
    <div>
      <JNavTop></JNavTop>
      <div class="container">
        <router-view v-if="Authenticate===false"></router-view>
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
    name: 'app_club',
    computed: {
      Authenticate () {
        return this.$store.state.Authenticated
      }
    }
  }
</script>

<style>
  #app_club .container {
    margin-right: auto;
    margin-left: auto;
    width: 100%;
  }
</style>
