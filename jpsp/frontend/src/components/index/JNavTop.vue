<!---component nav-top-->
<template>
  <div>
    <nav class="fh5co-nav" role="navigation">
      <div class="top-menu">
        <div class="container-fluid">
          <div class="row">
            <div class="col-xs-4">
              <div id="fh5co-logo"><a href="" class="title">建平中学学生平台</a></div>
            </div>
            <div class="col-xs-8 text-right menu-1">
              <ul>
                <li class="active"><a href="">首页</a></li>
                <li class="has-dropdown"><a href="">社团</a>
                  <ul class="dropdown">
                    <li><router-link to="/clublist">社团列表</router-link></li>
                    <li><router-link to="/club/event">社团动态</router-link></li>
                  </ul>
                </li>
                <li class="has-dropdown"><a href="">活动</a>
                  <ul class="dropdown">
                    <li><router-link to="/activity/list">活动报名</router-link></li>
                    <li><router-link to="/activity/news">活动动态</router-link></li>
                  </ul>
                </li>
                <li>
                  <router-link to="/lost">失物招领</router-link>
                </li>
                <li><a href="about.html">关于</a></li>
                <li v-if="Authenticate===true">欢迎，{{ GetUserName }}</li>
                <li class="btn-cta" v-if="Authenticate===false || Authenticate===null"><a href="#"><span>登录</span></a>
                </li>
                <li class="btn-cta" v-else><a href="#"><span>注销</span></a></li>
              </ul>
            </div>
          </div>
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
    methods: {},
    computed: {
      Authenticate () {
        return this.$store.state.Authenticated
      },
      GetUserName () {
        return this.$store.state.UserName
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
