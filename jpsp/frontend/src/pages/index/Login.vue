<template>
  <div>
    <div class="LoginForm">
      <el-row class="tac">
        <el-col :span=8 :offset=8>
          <h1 class="login-title">学生登录</h1>
          <el-form ref="LoginForm" :model="LoginForm" :rules="rules" v-if="Authenticate===null || Authenticate===false">
            <el-form-item label="用户名" :required=true>
              <el-input v-model="LoginForm.UserName" placeholder="用户名" autofocus=""></el-input>
            </el-form-item>
            <el-form-item label="密码" :required=true>
              <el-input type="password" v-model="LoginForm.Password" placeholder="密码">
              </el-input>
            </el-form-item>
            <br>
            <el-form-item>
              <el-button type="primary" @click="onSubmit" class="login-button">登陆</el-button>
            </el-form-item>
            <a href="http://baidu.com"><p style="text-align: right">忘记密码？</p></a>
            <el-form-item>
              <p v-if="Authentsicate===false">登陆失败</p>
            </el-form-item>
          </el-form>
          <p class="lead" v-if="Authenticate===true">已登录</p>
        </el-col>
      </el-row>
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
        },
        rules: {
          UserName: [
            { required: true, message: '请输入用户名', trigger: 'blur' }
          ],
          Password: [
            { required: true, message: '请输入密码', trigger: 'change' }
          ]
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
    },
    computed: {
      Authenticate () {
        return this.$store.state.Authenticated
      }
    }
  }
</script>

<style scoped>
  .LoginForm {
    margin-top: 5%;
    margin-bottom: 5%;
  }

  .login-title {
    text-align: center;
  }
  .login-button {
    width: 100%;
    height: 45px;
  }
</style>
