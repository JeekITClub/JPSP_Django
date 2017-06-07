<template>
  <nav class="navbar navbar-default">
    <div class="container">
      <div class="navbar-header">
        <a class="navbar-brand" href="#">建平中学学生平台</a>
      </div>
      <div id="navbar" class="navbar-collapse collapse">
        <ul class="nav navbar-nav">
          <li><router-link to="#">主页</router-link></li>
          <li><router-link to="about">关于</router-link></li>
          <li><router-link to="#">联系我们</router-link></li>
        </ul>
        <ul class="nav navbar-nav navbar-right" v-if="Authenticate===true">
          <li><a href="../">{{ ClubName }}</a></li>
          <li><router-link to="profile">资料修改</router-link></li>
          <li><a href="/">消息列表</a></li>
          <li><a href="/">注销</a></li>
        </ul>
        <ul class="nav navbar-nav navbar-right" v-if="Authenticate===false">
          <li><router-link to="/#">登入</router-link></li>
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
      /**
       * @return {boolean}
       */
      Authenticate () {
        return this.$store.state.Authenticated
      },
      /**
       *
       * @returns {*|string}
       * @constructor
       */
      ClubName () {
        return this.$store.state.UserName
      },
      /**
       *
       * @returns {computed.ClubId|string|*|ClubId}
       * @constructor
       */
      ClubId () {
        return this.$store.state.ClubId
      }
    }
  }
</script>
<style>

</style>
