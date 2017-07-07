<template>
  <div>
    <div class="container">
      <div class="row clearfix">
        <div class="col-md-12 column">
          <div class="jumbotron">
            <h1>
             {{ Club.ClubName }}
            </h1>
            <p>
             {{ Club.Introduction }}
            </p>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>
<script>
  import axios from 'axios'
  export default {
    data () {
      return {
        ClubId: this.$route.params.ClubId,
        Club: {}
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
    },
    mounted: function () {
      axios({
        method: 'POST',
        url: 'http://127.0.0.1:8000/api/public/club/get',
        // TODO: write views to get club
        data: JSON.stringify({
          Token: this.GetToken,
          ClubId: this.ClubId
        })
      }).then(function (response) {
        if (response.data.message === 'success') {
          this.Club = JSON.parse(response.data.data)
          console.log('success')
        } else {
          console.log('error')
        }
      }.bind(this))
    }
  }
</script>
<style scoped>
  @import url("//unpkg.com/element-ui@1.3.2/lib/theme-default/index.css");
</style>
