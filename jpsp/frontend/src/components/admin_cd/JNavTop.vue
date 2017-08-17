<template>
  <nav class="navbar ">
    <div class="navbar-brand">
      <a class="navbar-item" href="">
        建平中学学生平台
      </a>
    </div>

    <div id="navMenubd-example" class="navbar-menu">
      <div class="navbar-start">
        <router-link class="navbar-item " to="/about">
          关于
        </router-link>
        <router-link class="navbar-item " to="/contact">
          联系我们
        </router-link>
      </div>
      <div class="navbar-end">
        <div class="navbar-item has-dropdown is-hoverable" v-if="Authenticated === 'true'">
          <a class="navbar-link" href="">欢迎,{{ UserName }}</a>
          <div class="navbar-dropdown">
            <router-link class="navbar-item" to="/profile">
              修改信息
            </router-link>
            <a class="navbar-item" @click="logout">
              注销
            </a>
          </div>

        </div>
        <div class="navbar-item" v-else>
          <div class="field">
            <p class="control">
              <router-link to="/login">登陆</router-link>
            </p>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>
<script>
  export default {
    data () {
      return {}
    },
    methods: {
      logout () {
        this.$cookie.delete('CDAuthenticated')
        this.$cookie.delete('CDToken')
      }
    },
    computed: {
      Authenticated () {
        return this.$cookie.get('CDAuthentiacated')
      },
      UserName () {
        return this.$cookie.get('CDUserName')
      }
    }
  }
</script>
<style>

</style>
