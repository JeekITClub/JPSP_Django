<!---component nav-top-->
<template>
  <div>
    <nav class="navbar">
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
            <router-link class="navbar-link " to="/Club">
              社团
            </router-link>
            <div class="navbar-dropdown ">
              <router-link class="navbar-item " to="/Club">
                社团列表
              </router-link>
              <!--<router-link class="navbar-item " to="/Club/Event">-->
                <!--社团动态-->
              <!--</router-link>-->
            </div>
          </div>
          <!--<div class="navbar-item has-dropdown is-hoverable">-->
            <!--<router-link class="navbar-link " to="/Activity">-->
              <!--活动-->
            <!--</router-link>-->
            <!--<div id="blogDropdown" class="navbar-dropdown " data-style="width: 18rem;">-->
              <!--<router-link class="navbar-item " to="/Activity/list">-->
                <!--活动报名-->
              <!--</router-link>-->
              <!--<router-link class="navbar-item " to="/Activity/">-->
                <!--活动动态-->
              <!--</router-link>-->
            <!--</div>-->
          <!--</div>-->
          <!--<a class="navbar-item" href="#">-->
            <!--失物招领-->
          <!--</a>-->
        </div>

        <div class="navbar-end">
          <div class="navbar-item has-dropdown is-hoverable" v-if="GetIndexAuthenticated === 'true'">
            <router-link class="navbar-link " to="/User/Dashboard">
              欢迎你，{{ GetUserName }}
            </router-link>
            <div class="navbar-dropdown" data-style="width: 18rem;">
              <router-link to="/User/Dashboard" class="navbar-item ">个人中心</router-link>
              <a @click="Logout" class="navbar-item ">注销</a>
            </div>
          </div>
          <div class="navbar-item has-dropdown is-hoverable" v-else>
            <router-link class="navbar-link " to="/Login">
              登录
            </router-link>
            <div class="navbar-dropdown">
              <router-link class="navbar-item" to="/Login">
                学生登录
              </router-link>
              <!--TODO: Link to admin_club & admin_cd-->
              <router-link class="navbar-item " to="http://119.23.49.42/admin_club/">
                社长登录
              </router-link>
              <router-link class="navbar-item " to="http://119.23.49.42/admin_cd/">
                社团部登录
              </router-link>
            </div>
          </div>
          <router-link class="navbar-item" to="/About">
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
        try {
          this.$cookie.delete('UserId')
          this.$cookie.delete('IndexToken')
          this.$cookie.delete('UserName')
          this.$cookie.delete('IndexAuthenticated')
          this.$router.push('/')
          location.reload(true)
        } catch (e) {
          this.$notify.error({
            title: '错误',
            message: '注销失败'
          })
        }
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
    }
  }
</script>
<style scoped>
  .jpsp {
    width:100%;
    height:30px;
    background: transparent;
    position:fixed;
    top:0;
    left:0;
  }
</style>
