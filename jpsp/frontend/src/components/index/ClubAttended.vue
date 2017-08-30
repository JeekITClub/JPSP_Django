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
          <a class="card-footer-item" @click="quitClub(Club.ClubId)" v-if="Club.State === '1'">
            <p>我想退出</p>
          </a>
          <a class="card-footer-item" @click="quitClub(Club.ClubId)" v-else>
            <p>我想退出（审核中）</p>
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
      GetUserIndexId () {
        return this.$cookie.get('UserIndexId')
      },
      GetIndexToken () {
        return this.$cookie.get('IndexToken')
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
          url: this.GetApi + 'clubships/user',
          data: Qs.stringify({
            UserIndexId: this.GetUserIndexId,
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
        url: this.GetApi + 'clubships/user',
        params: {
          UserId: this.GetUserIndexId
        },
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        }
      })
        .then(function (response) {
          if (response.data.message === 'success') {
            this.Clubs = response.data.data
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
