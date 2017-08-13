<template>
  <div>
    <div class="LoginForm">
      <el-row class="tac">
        <el-col :span=8 :offset=8>
          <h1 class="login-title">学生登录</h1>
          <div v-if="Authenticated != true">
            <el-form ref="LoginForm" :model="LoginForm" :rules="Rules">
              <el-form-item label="用户名" prop="UserName">
                <el-input v-model="LoginForm.UserName" placeholder="用户名" autofocus=""></el-input>
              </el-form-item>
              <el-form-item label="密码" prop="Password">
                <el-input type="password" v-model="LoginForm.Password" placeholder="密码">
                </el-input>
              </el-form-item>
              <br>
              <el-form-item>
                <el-button type="primary" @click="onSubmit" class="login-button">登录</el-button>
              </el-form-item>
              <p style="text-align: right;">
                <router-link to="/contact">忘记密码？</router-link>
              </p>
            </el-form>
          </div>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
  import { getCookie, setCookie } from 'tiny-cookie'
  import axios from 'axios'
  export default {
    data () {
      return {
        LoginForm: {
          UserName: '',
          Password: ''
        },
        Rules: {
          UserName: [
            {required: true, message: '请输入用户名', trigger: 'blur'}
          ],
          Password: [
            {required: true, message: '请输入密码', trigger: 'blur'}
          ]
        }
      }
    },
    methods: {
      onSubmit () {
        this.$refs['LoginForm'].validate((valid) => {
          if (valid) {
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
                  let expireDays = 1000 * 60 * 60 * 24 * 3
                  setCookie('UserId', this.LoginForm.UserName, expireDays)
                  setCookie('UserName', response.data.UserName, expireDays)
                  setCookie('IndexToken', response.data.Token, expireDays)
                  // expireDays 为有效时间
                  setCookie('IndexAuthenticated', true, expireDays)
                  // 第一个值为key，第二个为value，第三个为有限时间
                  this.$router.push('/')
//                this.$store.commit('Authenticated', true)
//                this.$store.commit('ApplyUserName', response.data.UserName)
//                this.$store.commit('ApplyToken', response.data.Token)
                } else if (response.data.message === 'User Not Authenticated') {
                  this.$notify.error({
                    title: '错误',
                    message: '登陆失败'
                  })
                }
              }.bind(this))
          } else {
            alert('error')
          }
        })
      },
      checkLogin () {
        if (getCookie('IndexAuthenticated') === 'true') {
          this.$router.push('/')
        } else {
          this.$router.push('/login')
        }
      }
    },
    computed: {
      Authenticated () {
        return getCookie('IndexAuthenticated')
      },
      /**
       * @return {string}
       */
      GetApi () {
        return this.$store.state.Api
      }
    },
    created () {
      this.checkLogin()
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
