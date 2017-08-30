<template>
<div>

  <div class="columns is-multiline is-mobile jpsp-ac">
    <div class="column is-one-quarter" v-for="Club in Clubs">
      <div class="card">
        <div class="card-image">
          <figure class="image is-1by1">
            <img src="../../assets/dp.jpg">
          </figure>
        </div>

        <div class="card-content">
          <div class="content">
            <h3 class="title is-3">{{ Club.ClubName }}</h3>
          </div>
        </div>
        <footer class="card-footer">
          <a class="card-footer-item" @click="quitClub(Club.ClubId)">
            <p>我想退出</p>
          </a>
        </footer>
      </div>
    </div>
  </div>

  </div>
</template>
<script>
  import axios from 'axios'
  import Qs from 'qs'
  export default {
    data () {
      return {
        Clubs: []
      }
    },
    computed: {
      GetUserId () {
        return this.$cookie.get('UserId')
      },
      GetIndexToken () {
        return this.$cookie.get('IndexToken')
      },
      GetUserName () {
        return this.$cookie.get('UserName')
      },
      GetIndexAuthenticated () {
        return this.$cookie.get('IndexAuthenticated')
      },
      /**
       * @return {string}
       */
      GetApi () {
        return this.$store.state.Api
      }
    },
    methods: {
      quitClub (ClubId) {
        axios({
          method: 'DELETE',
          url: this.GetApi + '',
          data: Qs.stringify({
            UserId: this.GetUserId,
            Token: this.GetIndexToken,
            ClubId: ClubId
          }),
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
          }
        })
          .then(function (response) {
            if (response.data.message === 'success') {
              this.$notify({
                'title': '成功',
                'message': '成功退出社团',
                'type': 'success'
              })
            } else {
              this.$notify.error({
                title: '错误',
                message: '无法获得数据'
              })
            }
          }.bind(this))
      },
      checkLogin () {
        if (this.$cookie.get('IndexAuthenticated') !== 'true') {
          this.$router.push('/login')
        }
      }
    },
    created () {
      this.checkLogin()
    },
    mounted: function () {
      axios({
        method: 'GET',
        url: this.GetApi + '',
        params: {
          UserId: this.GetUserId
        },
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        }
      })
        .then(function (response) {
          if (response.data.message === 'success') {
            this.Clubs = response.data.ClubLsit
            // TODO: API / getClubshipByUserId
          } else {
            this.$notify.error({
              title: '错误',
              message: '无法获得数据'
            })
          }
        }.bind(this))
    }
  }
</script>
<style scoped>
  .jpsp-ac {
    padding-top: 2%;
    padding-right: 2%;
  }
</style>
