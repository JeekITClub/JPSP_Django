<template>
  <nav class="navbar navbar-default">
    <div class="container">
      <div class="navbar-header">
        <a class="navbar-brand" href="#">建平中学学生平台</a>
      </div>
      <div id="navbar" class="navbar-collapse collapse">
        <ul class="nav navbar-nav">
          <li>
            <router-link to="/">主页</router-link>
          </li>
          <li>
            <router-link to="about">关于</router-link>
          </li>
          <li>
            <router-link to="contact">联系我们</router-link>
          </li>
        </ul>
        <ul class="nav navbar-nav navbar-right" v-if="Authenticated === true">
          <li>{{ ClubName }}</li>
          <li>
            <router-link to="profile">资料修改</router-link>
          </li>
          <li><a @click="logout()">注销</a></li>
        </ul>
        <ul class="nav navbar-nav navbar-right" v-if="Authenticated != true">
          <li>
            <router-link to="/login">登入</router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>
<script>
  import {getCookie, removeCookie} from 'tiny-cookie'
  export default {
    data () {
      return {}
    },
    methods: {
      logout () {
        removeCookie('ClubAuthenticated')
        removeCookie('ClubName')
        removeCookie('ClubId')
        removeCookie('ClubToken')
      }
    },
    computed: {
      /**
       * @return {boolean}
       */
      Authenticated () {
        return getCookie('ClubAuthenticated')
      },
      ClubName () {
        return getCookie('ClubName')
      },
      ClubId () {
        return getCookie('ClubId')
      }
    }
  }
</script>
<style>
</style>
