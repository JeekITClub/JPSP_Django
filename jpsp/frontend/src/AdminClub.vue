<template>
  <div id="app_club">
    <JNavTop></JNavTop>
    <div class="container">
      <!-- <el-row class="tac" :gutter="20" v-if="Authenticated === true"> -->
      <el-row class="tac" :gutter="20">
        <el-col :span="4">
          <club-aside></club-aside>
        </el-col>
        <el-col :span="20">
          <router-view></router-view>
        </el-col>
      </el-row>
      <!-- <el-row class="tac" v-else>
        <router-view></router-view>
      </el-row> -->
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

  #app_club .container {
    margin-right: auto;
    margin-left: auto;
    width: 100%;
  }
</style>
