<!---component nav-top-->
<template>
  <div>
    <nav class="fh5co-nav" role="navigation">
      <div class="top-menu">
        <div class="container-fluid">
          <div class="row">
            <div class="col-xs-4">
              <div>
                <img src="../../assets/ICON.png" style="width:80%;height: 80%">
              </div>
            </div>
            <div class="col-xs-8 text-right menu-1">
              <ul>
                <li><a href="">首页</a></li>
                <li class="has-dropdown">
                  <router-link to="/club">社团</router-link>
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
                  <router-link to="/activity/list">活动</router-link>
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
                <li v-if="GetAuthenticated === 'true'">欢迎，{{ GetUserName }}</li>
                <li v-if="GetAuthenticated === 'true'"><router-link to="/profile">资料修改</router-link></li>
                <li class="has-dropdown" v-if="GetAuthenticated !== 'true'">
                  <router-link to="/login">登录</router-link>
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
                <li class="btn-cta" v-if="GetAuthenticated === 'true'"><a href="#"><span>注销</span></a></li>
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
    methods: {},
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
