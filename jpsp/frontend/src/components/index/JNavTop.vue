<!---component nav-top-->
<template>
  <div class="container">
    <nav class="navbar jpsp-nav">
      <div class="navbar-brand">
        <a class="navbar-item" href="">
          建平中学学生平台
        </a>
        <div class="navbar-burger" data-target="navMenu">
          <span></span>
          <span></span>
          <span></span>
        </div>

      </div>
      <div id="navMenu" class="navbar-menu">
        <div class="navbar-start">
          <div class="navbar-item has-dropdown is-hoverable">
            <router-link class="navbar-link " to="/club">
              社团
            </router-link>
            <div class="navbar-dropdown ">
              <router-link class="navbar-item " to="/club">
                社团列表
              </router-link>
              <router-link class="navbar-item " to="/club/event">
                社团动态
              </router-link>
            </div>
          </div>
          <div class="navbar-item has-dropdown is-hoverable">
            <router-link class="navbar-link " to="/activity">
              活动
            </router-link>
            <div id="blogDropdown" class="navbar-dropdown " data-style="width: 18rem;">
              <router-link class="navbar-item " to="/activity/list">
                活动报名
              </router-link>
              <router-link class="navbar-item " to="/activity/">
                活动动态
              </router-link>


            </div>
          </div>
          <a class="navbar-item" href="#">
            失物招领
          </a>
        </div>

        <div class="navbar-end">
          <div class="navbar-item has-dropdown is-hoverable">
            <router-link class="navbar-link  is-active" to="/login">
              登录
            </router-link>
            <div class="navbar-dropdown">
              <router-link class="navbar-item" to="/login">
                登录
              </router-link>
              <router-link class="navbar-item " to="http://119.23.49.42/admin_club/">
                社长登录
              </router-link>
              <router-link class="navbar-item " to="http://119.23.49.42/admin_cd/">
                社团部登录
              </router-link>
            </div>
          </div>
          <router-link class="navbar-item" to="/about">
            关于
          </router-link>
        </div>
      </div>
    </nav>
  </div>
</template>
<script>
  export default {
    data () {
      return {}
    },
    methods: {
      Logout () {
        // TODO: 注销
        console.log('谁点谁傻逼')
      }
    },
    computed: {
      GetAuthenticated () {
        return this.$cookie.get('IndexAuthenticated')
      },
      GetUserName () {
        return this.$cookie.get('IndexUserName')
      }
    }
  }
</script>
<style scoped>
</style>
