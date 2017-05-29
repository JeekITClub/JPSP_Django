<template>
  <nav class="navbar navbar-default">
    <div class="container">
      <div class="navbar-header">
        <a class="navbar-brand" href="#">建平中学社团系统</a>
      </div>
      <div id="navbar" class="navbar-collapse collapse">
        <ul class="nav navbar-nav">
          <li><a href="#">主页</a></li>
          <li><a href="#">关于我们</a></li>
          <li><a href="#">联系我们</a></li>
        </ul>
        <ul class="nav navbar-nav navbar-right" v-if="LoginIn===true">
          <li><a href="../">{{ ClubName }}</a></li>
          <li><a href="../">资料修改</a></li>
          <li><a href="../">消息列表</a></li>
          <li><a href="../">退出登录</a></li>
        </ul>
        <ul class="nav navbar-nav navbar-right" v-if="LoginIn===false">
          <li><a href="">登入</a></li>
        </ul>
      </div><!--/.nav-collapse -->
    </div><!--/.container-fluid -->
  </nav>
</template>
<script>
  export default {
    data () {
      return {}
    },
    methods: {
      handleSelect (key, keyPath) {
        console.log(key, keyPath)
      }
    },
    computed: {
      LoginIn () {
        return this.$store.state.Login_in
      },
      ClubName () {
        return this.$store.state.ClubName
      },
      ClubId () {
        return this.$store.state.ClubId
      }
    }
  }
</script>
<style>

</style>
