<template>
  <div>
    <h1>学生登录</h1>
    <el-form ref="LoginForm" :model="LoginForm">
      <el-form-item label="学号">
        <el-input type="text" v-model="LoginForm.UserId"></el-input>
      </el-form-item>
      <el-form-item label="密码">
        <el-input type="password" v-model="LoginForm.Password"></el-input>
      </el-form-item>
      <el-button type="primary" @click="onSubmit">登陆</el-button>
    </el-form>
  </div>
</template>

<script>
  import axios from 'axios'
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
          url: 'http://127.0.0.1:8000/api/login',
          data: JSON.stringify({
            UserName: this.LoginForm.UserId,
            Password: this.LoginForm.Password,
            UserType: 'Student'
          })
        })
          .then(function (response) {
            if (response.data.message === 'User Authenticated') {
              this.$store.commit('Authenticated', true)
              this.$store.commit('ApplyUserName', response.data.UserName)
              this.$store.commit('ApplyToken', response.data.Token)
            } else if (response.data.message === 'User Not Authenticated') {
              console.log('Login Failed')
            }
          }.bind(this))
          .catch(function (error) {
            console.log(error)
          })
      }
    }
  }
</script>

<style scoped>
  @import '../../assets/index/css/bootstrap.css';
  @import '../../assets/index/css/login.css';
</style>
