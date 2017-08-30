<template>
  <div class="container">
    <h3 class="title is-3" align="center">更改密码</h3>
    <div class="ch">
      <div class="field">
        <label class="label">原密码</label>
        <div class="control">
          <input class="input" type="password" v-model="OriginalPassword">
        </div>
      </div>

      <div class="field">
        <label class="label">新密码</label>
        <div class="control">
          <input class="input" type="password" v-model="NewPassword">
        </div>
      </div>

      <div class="field">
        <label class="label">确认新密码</label>
        <div class="control">
          <input class="input" type="password" v-model="ConfirmNewPassword">
        </div>
      </div>

      <div class="field">
        <div class="control">
          <button class="button is-primary is-medium" @click="submitForm">提交</button>
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
        OriginalPassword: '',
        NewPassword: '',
        ConfirmNewPassword: ''
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
      checkLogin () {
        if (this.$cookie.get('IndexAuthenticated') !== 'true') {
          this.$router.push('/login')
        }
      },
      submitForm () {
        if (this.OriginalPassword === this.NewPassword) {
          this.$notify.error({
            title: '错误',
            message: '新密码与原密码相同'
          })
        } else if (this.NewPassword !== this.ConfirmNewPassword) {
          this.$notify.error({
            title: '错误',
            message: '确认密码与新密码不同'
          })
        } else {
          axios({
            method: 'PUT',
            url: this.GetApi + 'users/password',
            data: Qs.stringfy({
              UserId: this.GetUserId,
              Password: this.NewPassword
            }),
            headers: {
              'Content-Type': 'application/x-www-form-urlencoded'
            }
          })
            .then(function (response) {
              if (response.data.message === 'success') {
                this.$notify({
                  title: '成功',
                  message: '成功更改密码',
                  type: 'success'
                })
              }
              if (response.data.message === 'error') {
                this.$notify.error({
                  title: '错误',
                  message: '无法更改密码'
                })
              }
            }.bind(this))
            .catch(function () {
              this.$notify.error({
                'title': '错误',
                'message': '无法更改密码'
              })
            }.bind(this))
        }
      }
    },
    created () {
      this.checkLogin()
    }
  }
</script>
<style scoped>
  .ch {
    padding-left: 20%;
    padding-right: 20%;
    padding-bottom: 5%;
  }
</style>
