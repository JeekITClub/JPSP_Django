<template>
<div>
  <h1>这是{{ Club.ClubName }}社的主页</h1>
</div>
</template>
<script>
  // TODO: data will disappear after F5
  export default {
    data () {
      return {
        Club: this.$route.params.Club
      }
    },
    computed: {
      Authenticate () {
        return this.$store.state.Authenticated
      },
      GetUserName () {
        return this.$store.state.UserName
      },
      GetToken () {
        return this.$store.state.Token
      }
    }
  }
</script>
<style scoped>
  @import url("//unpkg.com/element-ui@1.3.2/lib/theme-default/index.css");
</style>
