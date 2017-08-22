<template>
<div>

  <div class="columns is-multiline is-mobile jpsp-ac">
    <div class="column is-one-quarter" v-for="Club in ProfileForm.Club">
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
          <a class="card-footer-item" @click="quitClub">
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
  export default {
    data () {
      return {
        ProfileForm: {
          UserName: '',
          Grade: '',
          Class: '',
          QQ: '',
          Email: '',
          Phone: '',
          Club: [
            {
              ClubId: '233',
              ClubName: 'Jeek'
            }
          ],
          AttendYear: ''
        }
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
        // TODO: delete club from tuple(Club)
        axios({
          method: 'POST',
          url: this.GetApi + 'club/quit',
          data: JSON.stringify({
            UserId: this.GetUserId,
            IndexToken: this.GetIndexToken,
            ClubId: ClubId
          })
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
        method: 'POST',
        url: this.GetApi + 'user/profile/get',
        data: JSON.stringify({
          UserId: this.GetUserId,
          Token: this.GetIndexToken
        })
      })
        .then(function (response) {
          if (response.data.message === 'success') {
            this.ProfileForm = JSON.parse(response.data.data)
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
