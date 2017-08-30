<template>
  <div class="">
    <div class="LoginForm">
      <el-form ref="LoginForm" :model="LoginForm">
        <el-form-item :required=true>
          <label class="label">社团ID</label>
          <input class="input" v-model="LoginForm.ClubId" placeholder="社团ID" autofocus="">
        </el-form-item>
        <el-form-item :required=true>
          <label class="label">密码</label>
          <input class="input" type="password" v-model="LoginForm.Password" placeholder="密码">
        </el-form-item>
        <el-form-item>
          <a class="button is-primary" @click="onSubmit">登陆</a>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>
<script>
  import axios from 'axios'
  import Qs from 'qs'

  export default {
    data () {
      return {
        LoginForm: {
          ClubId: '',
          Password: ''
        }
      }
    },
    methods: {
      onSubmit () {
        axios({
          method: 'POST',
          url: this.GetApi + 'auth/login',
          data: Qs.stringify({
            UserId: this.LoginForm.ClubId,
            Password: this.LoginForm.Password,
            UserType: 'Club'
          }),
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
          }
        })
          .then(function (response) {
            console.log(response)
            if (response.data.message === 'success') {
              this.$cookie.set('ClubId', this.LoginForm.ClubId, 1)
              this.$cookie.set('ClubName', response.data.ClubName, 1)
              this.$cookie.set('ClubToken', response.data.Token, 1)
              this.$cookie.set('ClubAuthenticated', true, 1)
              this.$router.push('/Dashboard')
              location.reload(true)
            } else {
              this.$notify.error({
                title: '错误',
                message: '登陆失败'
              })
            }
          }.bind(this))
      }
    },
    computed: {
      GetClubId () {
        return this.$cookie.get('ClubId')
      },
      GetIndexToken () {
        return this.$cookie.get('ClubToken')
      },
      GetUserName () {
        return this.$cookie.get('ClubName')
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
    }
  }
</script>
<style>
  .LoginForm {
    margin-top: 13%;
  }
</style>
