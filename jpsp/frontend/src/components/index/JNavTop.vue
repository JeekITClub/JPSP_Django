<!---component nav-top-->
<template>
  <div class="container">
    <nav class="navbar jpsp-nav">
      <div class="navbar-brand">
        <a class="navbar-item" href="http://bulma.io">
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
            <div class="navbar-dropdown">
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
