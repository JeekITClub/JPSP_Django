<template>
  <div id="app_cd">
    <j-nav-top></j-nav-top>
    <el-row class="tac" v-if="Authenticated === true">
      <el-col :span=4>
        <c-d-aside></c-d-aside>
      </el-col>
      <el-col :span=20>
        <transition>
          <router-view></router-view>
        </transition>
      </el-col>
    </el-row>
    <el-row class="tac" v-else-if="Authenticated != true">
        <router-view></router-view>
    </el-row>
  </div>
</template>

<script>
  import JNavTop from '@/components/admin_cd/JNavTop.vue'
  import CDAside from '@/components/admin_cd/CDAside.vue'
  import {getCookie} from 'tiny-cookie'
  export default {
    components: {
      'JNavTop': JNavTop,
      'CDAside': CDAside
    },
    name: 'app_cd',
    computed: {
      Authenticated () {
        return getCookie('CDAuthentiacated')
      }
    }
  }
</script>

<style>
  #app_cd .container {
    margin-right: auto;
    margin-left: auto;
    width: 100%;
  }
</style>
