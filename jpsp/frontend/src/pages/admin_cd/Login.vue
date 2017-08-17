<template>
  <div class="">
    <div class="LoginForm">
      <el-form ref="LoginForm" :model="LoginForm">
        <el-form-item :required=true>
          <label class="label">用户名</label>
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
          url: 'http://127.0.0.1:8000/api/login',
          data: JSON.stringify({
            UserName: this.LoginForm.UserName,
            Password: this.LoginForm.Password
          })
        }).then(function (response) {
          if (response.data.message === 'User Authenticated') {
            this.$store.commit('Authenticate', true)
            this.$store.commit('ApplyUserName', this.UserName)
            this.$store.commit('ApplyToken', response.data.Token)
          } else if (response.data.message === 'User Not Authenticated') {
            this.$store.commit('Authenticate', false)
          }
        }.bind(this))
          .catch(function (error) {
            console.log(error)
          })
      }
    }
  }
</script>
<style>
  .LoginForm {
    margin-top: 13%;
  }
</style>
