<template>
<div>
<aside class="menu">
  <p class="menu-label">
    用户设置
  </p>
  <ul class="menu-list">
    <li><a class="jpsp-menu-item">基本信息</a></li>
    <li><a class="jpsp-menu-item">更改密码</a></li>
  </ul>
  <p class="menu-label">
    社团
  </p>
  <ul class="menu-list">
    <li><a class="jpsp-menu-item">已加入社团</a></li>
  </ul>
  <p class="menu-label">
    活动
  </p>
  <ul class="menu-list">
    <li><a class="jpsp-menu-item">已加入活动</a></li>
    <li><a class="jpsp-menu-item">参加过的活动</a></li>
  </ul>
</aside>
  </div>
</template>
<script>
  export default {
    data () {
      return {
      }
    },
    computed: {
      GetUserId () {
        return this.$cookie.get('UserId')
      },
      GetIndexToken () {
        return this.$cookie.get('IndexToken')
      },
      GetUserName () {
        return this.$cookie.get('UserName')
      },
      GetIndexAuthenticated () {
        return this.$cookie.get('IndexAuthenticated')
      },
      /**
       * @return {string}
       */
      GetApi () {
        return this.$store.state.Api
      }
    },
    methods: {
      checkLogin () {
        if (this.$cookie.get('IndexAuthenticated') !== 'true') {
          this.$router.push('/login')
        }
      }
    }
    // ,
    // created () {
    //   this.checkLogin()
    // }
  }
</script>
<style scoped>
  .select-title {
    padding-left: 20px;
  }

  .jpsp-profile {
    padding-top: 2%;
  }
</style>
