<template>
<section class="hero is-info is-fullheight">
  <div class="hero-body">
    <div class="container">
      <h1 class="title">
        建平学生平台
      </h1>
      <h2 class="subtitle">
        Jianping Students' Platform
      </h2>
    </div>
  </div>
</section>
</template>
<script>
  import { getCookie } from 'tiny-cookie'
  export default {
    data () {
      return {}
    },
    methods: {},
    computed: {
      GetUserId () {
        return getCookie('UserId')
      },
      GetIndexToken () {
        return getCookie('IndexToken')
      },
      GetUserName () {
        return getCookie('UserName')
      },
      GetIndexAuthenticated () {
        return getCookie('IndexAuthenticated')
      },
      /**
       * @return {string}
       */
      GetApi () {
        return this.$store.state.Api
      }
    }
  }
</script>
<style scoped>
</style>
