<template>
  <p class="lead" style="text-align: center">该页面已被WTO遗弃 2017/7/28</p>
</template>
<script>
  import axios from 'axios'
  export default {
    data () {
      return {
        LoginForm: {
          UserName: '',
          Password: ''
        }
      }
    },
    methods: {
      onSubmit () {
        axios({
          method: 'POST',
          url: this.GetApi + 'login',
          data: JSON.stringify({
            UserName: this.LoginForm.UserName,
            Password: this.LoginForm.Password,
            UserType: 'Student'
          })
        })
          .then(function (response) {
            if (response.data.message === 'User Authenticated') {
              this.$cookie.set('UserId', this.LoginForm.UserName, 1)
              this.$cookie.set('UserName', response.data.UserName, 1)
              this.$cookie.set('IndexToken', response.data.Token, 1)
              this.$cookie.set('IndexAuthenticated', true, 1)
              this.$router.push('/')
            } else if (response.data.message === 'User Not Authenticated') {
              this.$notify.error({
                title: '错误',
                message: '登陆失败'
              })
            }
          }.bind(this))
      }
    },
    computed: {
      GetUserId () {
        return this.$cookie.get('UserId')
      },
      GetIndexToken () {
        return this.$cookie.get('ClubToken')
      },
      GetUserName () {
        return this.$cookie.get('UserName')
      },
      GetIndexAuthenticated () {
        return this.$cookie.get('ClubAuthenticated')
      },
      /**
       * @return {string}
       */
      GetApi () {
        return this.$store.state.Api
      }
    },
    created: function () {
      if (this.$cookie.get('ClubAuthenticated') === 'true') {
        this.$router.push('/')
      }
    }
  }
</script>
<style>
</style>
