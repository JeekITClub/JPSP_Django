<template>
<div>
  <div class="columns jpsp-profile">
    <div class="column">
      <div class="tile is-ancestor">
        <div class="tile is-vertical is-8">
          <div class="tile">
            <div class="tile is-parent is-vertical">
              <article class="tile is-child notification is-primary">
                <p class="title">学号</p>
                <p class="subtitle">{{ GetUserId }}</p>
              </article>
              <article class="tile is-child notification is-warning">
                <p class="title">用户名</p>
                <p class="subtitle">{{ GetUserName }}</p>
              </article>
            </div>
            <div class="tile is-parent">
              <article class="tile is-child notification is-info">
                <p class="title">头像</p>
                <p class="subtitle">就这点经费还想有头像？</p>
                <figure class="image is-4by3">
                  <img src="http://bulma.io/images/placeholders/640x480.png">
                </figure>
              </article>
            </div>
          </div>
          <div class="tile is-parent">
            <article class="tile is-child notification is-danger">
              <p class="title">个人介绍</p>
              <p class="subtitle">建平的一个普通学生</p>
              <div class="content">
                <!-- Content -->
              </div>
            </article>
          </div>
        </div>
        <div class="tile is-parent">
          <article class="tile is-child notification is-success">
            <div class="content">
              <p class="title">最近通知</p>
              <p class="subtitle">我的社团最近干了些什么？</p>
              <div class="content">
                <!-- Content -->
              </div>
            </div>
          </article>
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
        ProfileForm: {
          UserName: '',
          Grade: '',
          Class: '',
          QQ: '',
          Email: '',
          Phone: '',
          Club: [],
          AttendYear: ''
//          Activity: [
//            [],
//            []
//          ]
        },
        activeIndex: '1'
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
      /**
       * @return {string}
       */
      GetApi () {
        return this.$store.state.Api
      }
    },
    methods: {
      checkLogin () {
        if (this.$cookie.get('IndexAuthenticated') !== 'true') {
          this.$router.push('/login')
        }
      }
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
    },
    created () {
      this.checkLogin()
    }
  }
</script>
<style scoped>
  .jpsp-profile {
    padding-top: 2%;
    padding-right: 2%;
  }
</style>
