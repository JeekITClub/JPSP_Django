<template>
</template>

<script>
  import axios from 'axios'
  export default {
    data () {
      return {
        ClubListTable: []
      }
    },
    mounted: function () {
      axios({
        method: 'POST',
        url: 'http://127.0.0.1:8000/api/public/club/list',
        data: JSON.stringify({
          Token: this.GetToken
        })
      }).then(function (response) {
        if (response.data.message === 'success') {
          this.ClubListTable = JSON.parse(response.data.data)
          console.log('success')
        } else {
          console.log('error')
        }
      }.bind(this))
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
<style>
  @import url("//unpkg.com/element-ui@1.3.2/lib/theme-default/index.css");
</style>
