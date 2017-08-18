<template>
  <div id="app_cd">
    <j-nav-top></j-nav-top>
    <div class="columns" v-if="Authenticated !== true">
      <div class="column is-1 cd-aside">
        <c-d-aside></c-d-aside>
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
  import JNavTop from '@/components/admin_cd/JNavTop.vue'
  import CDAside from '@/components/admin_cd/CDAside.vue'
  export default {
    components: {
      'JNavTop': JNavTop,
      'CDAside': CDAside
    },
    name: 'app_cd',
    computed: {
      Authenticated () {
        return this.$cookie.get('CDAuthentiacated')
      }
    }
  }
</script>

<style>
  #app_cd {
    margin-left: 2%;
    margin-right: 2%;
  }
</style>
