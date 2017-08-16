<!---component nav-top-->
<template>
  <div>
    <nav class="fh5co-nav" role="navigation">
      <div class="top-menu">
        <div class="container-fluid">
          <div class="row">
            <div class="col-xs-4">
              <div>
                <img src="../../assets/ICON.png" style="width:60%;height: 60%">
              </div>
            </div>
            <div class="col-xs-8 text-right menu-1">
              <ul>
                <li><a href="">首页</a></li>
                <li class="has-dropdown">
                  <a>社团</a>
                  <ul class="dropdown">
                    <li>
                      <router-link to="/club">社团列表</router-link>
                    </li>
                    <li>
                      <router-link to="/club/event">社团动态</router-link>
                    </li>
                  </ul>
                </li>
                <li class="has-dropdown">
                  <a>活动</a>
                  <ul class="dropdown">
                    <li>
                      <router-link to="/activity/list">活动报名</router-link>
                    </li>
                    <li>
                      <router-link to="/activity/news">活动动态</router-link>
                    </li>
                  </ul>
                </li>
                <li>
                  <router-link to="/lost">失物招领</router-link>
                </li>
                <li>
                  <router-link to="/about">关于</router-link>
                </li>
                <li v-if="GetAuthenticated === 'true'" class="has-dropdown">欢迎，{{ GetUserName }}<i class="icon-user"></i>
                  <ul class="dropdown">
                    <li>
                      <router-link to="/profile">个人中心</router-link>
                    </li>
                    <li>
                      <a @click="Logout">注销</a>
                    </li>
                  </ul>

                </li>
                <li class="has-dropdown" v-if="GetAuthenticated !== 'true'">
                  <a>登录</a>
                  <ul class="dropdown">
                    <li>
                      <router-link to="/login">学生登录</router-link>
                    </li>
                    <li>
                      <a href="../admin_club.html">社长登录</a>
                    </li>
                    <li>
                      <a href="../admin_cd.html">社团部登录</a>
                    </li>
                  </ul>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </nav>
  </div>
</template>
<script>
  import {getCookie} from 'tiny-cookie'
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
        return getCookie('IndexAuthenticated')
      },
      GetUserName () {
        return getCookie('UserName')
      }
    }
  }
</script>
<style scoped>
  @import '../../assets/index/css/animate.css';
  @import '../../assets/index/css/icomoon.css';
  @import '../../assets/index/css/bootstrap.css';
  @import '../../assets/index/css/magnific-popup.css';
  @import '../../assets/index/css/flexslider.css';
  @import '../../assets/index/css/style.css';
</style>
