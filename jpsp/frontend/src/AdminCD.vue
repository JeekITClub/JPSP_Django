<template>
  <div id="app_cd">
    <j-nav-top></j-nav-top>
    <el-row class="tac" v-if="Authenticate === true">
      <el-col :span=4>
        <c-d-aside></c-d-aside>
      </el-col>
      <el-col :span=20>
        <transition>
          <router-view></router-view>
        </transition>
      </el-col>
    </el-row>
    <el-row class="tac" v-if="Authenticate === null | false">
      <transition>
        <router-view></router-view>
      </transition>
    </el-row>
  </div>
</template>

<script>
  import JNavTop from '@/components/admin_cd/JNavTop.vue'
  import CDAside from '@/components/admin_cd/CDAside.vue'
  export default {
    components: {
      'JNavTop': JNavTop,
      'CDAside': CDAside
    },
    name: 'app_cd',
    computed: {
      Authenticate () {
        return this.$store.state.Authenticated
      }
    }
  }
</script>

<style>
</style>
