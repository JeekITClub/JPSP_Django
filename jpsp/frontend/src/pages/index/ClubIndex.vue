<template>
  <div>
    <div class="container">
      <div class="row clearfix">
        <div class="col-md-12 column">
          <div class="jumbotron">
            <h1>
              Jeek信息社
              {{ Club.ClubName }}
            </h1>
            <p>
              {{ Club.Introduction }}
             我们是xxx社，我们的目标是。。。
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
        url: 'http://127.0.0.1:8000/api/clubprofile/get',
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
</style>
