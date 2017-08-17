<!---component nav-top-->
<template>
  <div class="container">
    <nav class="navbar jpsp-nav">
  <div class="navbar-brand">
    <a class="navbar-item" href="http://bulma.io">
      <img src="http://bulma.io/images/bulma-logo.png" alt="Bulma: a modern CSS framework based on Flexbox" width="112" height="28">
    </a>

    <a class="navbar-item is-hidden-desktop" href="https://github.com/jgthms/bulma" target="_blank">
      <span class="icon" style="color: #333;">
        <i class="fa fa-github"></i>
      </span>
    </a>

    <a class="navbar-item is-hidden-desktop" href="https://twitter.com/jgthms" target="_blank">
      <span class="icon" style="color: #55acee;">
        <i class="fa fa-twitter"></i>
      </span>
    </a>

    <div class="navbar-burger burger" data-target="jpsp-menu">
      <span></span>
      <span></span>
      <span></span>
    </div>
  </div>

  <div id="jpsp-menu" class="navbar-menu">
    <div class="navbar-start">
      <div class="navbar-item has-dropdown is-hoverable">
        <a class="navbar-link " href="/documentation/overview/start/">
          社团
        </a>
        <div class="navbar-dropdown ">
          <a class="navbar-item " href="/documentation/overview/start/">
            社团列表
          </a>
          <a class="navbar-item " href="http://bulma.io/documentation/modifiers/syntax/">
            社团动态
          </a>
        </div>
      </div>
      <div class="navbar-item has-dropdown is-hoverable">
        <a class="navbar-link " href="http://bulma.io/blog/">
          活动
        </a>
        <div id="blogDropdown" class="navbar-dropdown " data-style="width: 18rem;">
          <a class="navbar-item " href="/documentation/overview/start/">
            活动报名
          </a>
          <a class="navbar-item " href="http://bulma.io/documentation/modifiers/syntax/">
            活动动态
          </a>


        </div>
      </div>
      <a class="navbar-item" href="#">
          失物招领
      </a>
    </div>

    <div class="navbar-end">
      <div class="navbar-item has-dropdown is-hoverable">
        <a class="navbar-link  is-active" href="/documentation/overview/start/">
          登录
        </a>
        <div class="navbar-dropdown ">
          <a class="navbar-item " href="/documentation/overview/start/">
            学生登录
          </a>
          <a class="navbar-item " href="http://bulma.io/documentation/modifiers/syntax/">
            社长登录
          </a>
          <a class="navbar-item " href="http://bulma.io/documentation/columns/basics/">
            社团部登录
          </a>
        </div>
      </div>
      <a class="navbar-item" href="#">
          关于
      </a>
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
</style>
