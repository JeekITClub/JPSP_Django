<template>
<div>
  <h1>所有动态</h1>
  <table class="table table-hover">
    <thead>
      <tr>
        <th>文章标题</th>
        <th>作者</th>
        <th>发布时间</th>
        <th>传送门</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for = "Post in Posts">
        <th>{{ Post.Title }}</th>
        <th>{{ Post.Author }}</th>
        <th>{{ Post.Time }}</th>
        <th><a href="">查看</a></th>
      </tr>
    </tbody>
  </table>
</div>
</template>
<script>
  export default {
    data () {
      return {
        // TODO: get all posts form backend
        Posts: [
          {title: '2333'},
          {title: '233333'},
          {title: '23333333'}
        ]
      }
    },
    computed: {
      Authenticate () {
        return this.$store.state.Authenticated
      },
      GetToken () {
        return this.$store.state.Token
      },
      GetUserName () {
        return this.$store.state.UserName
      }
    }
  }
</script>
<style scoped>
  @import url("//unpkg.com/element-ui@1.3.2/lib/theme-default/index.css");
  @import '../../assets/index/css/animate.css';
  @import '../../assets/index/css/icomoon.css';
  @import '../../assets/index/css/bootstrap.css';
  @import '../../assets/index/css/magnific-popup.css';
  @import '../../assets/index/css/flexslider.css';
  @import '../../assets/index/css/style.css';
</style>
