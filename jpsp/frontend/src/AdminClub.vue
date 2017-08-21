<template>
  <div id="app_club">
    <JNavTop></JNavTop>
    <div class="columns" v-if="Authenticated !== true">
      <div class="column is-2 club-aside">
        <club-aside></club-aside>
      </div>
      <div class="column">
        <router-view></router-view>
      </div>
    </div>
    <div class="columns" v-else>
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
  import ClubAside from '@/components/admin_club/ClubAside.vue'
  import JNavTop from '@/components/admin_club/JNavTop.vue'
  import { getCookie } from 'tiny-cookie'
  export default {
    components: {
      'ClubAside': ClubAside,
      'JNavTop': JNavTop
    },
    computed: {
      Authenticated () {
        return getCookie('ClubAuthenticated')
      }
    },
    name: 'app_club'
  }
</script>

<style>
  #app_club {
    margin-left: 2%;
    margin-right: 2%;
  }
</style>
