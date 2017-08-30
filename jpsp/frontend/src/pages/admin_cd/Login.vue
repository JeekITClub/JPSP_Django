<template>
  <div class="">
    <div class="LoginForm">
      <el-form ref="LoginForm" :model="LoginForm">
        <el-form-item :required=true>
          <label class="label">用户名</label>
          <input class="input" v-model="LoginForm.UserId" placeholder="社团ID" autofocus="">
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
          UserId: '',
          Password: ''
        }
      }
    },
    methods: {
      onSubmit () {
        axios({
          method: 'POST',
          url: this.GetApi + 'login',
          data: Qs.stringify({
            UserId: this.LoginForm.UserId,
            Password: this.LoginForm.Password,
            UserType: 'CD'
          }),
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
          }
        }).then(function (response) {
          if (response.data.message === 'success') {
            this.$cookie.set('CDAuthenticated', true, 1)
            this.$cookie.set('CDUserId', this.LoginForm.UserId, 1)
            this.$cookie.set('CDUserName', response.data.UserName, 1)
            this.$cookie.set('CDToken', response.data.Token, 1)
            location.reload(true)
          } else {
            this.$notify.error({
              title: '错误',
              message: '登陆失败'
            })
          }
        }.bind(this))
          .catch(function (error) {
            console.log(error)
          })
      }
    },
    computed: {
      GetUserId () {
        return this.$cookie.get('CDUserId')
      },
      GetCDToken () {
        return this.$cookie.get('CDToken')
      },
      GetUserName () {
        return this.$cookie.get('CDUserName')
      },
      GetCDAuthenticated () {
        return this.$cookie.get('CDAuthenticated')
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
