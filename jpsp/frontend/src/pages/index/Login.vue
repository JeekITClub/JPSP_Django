<template>
  <div>
    <div class="LoginForm">
      <h1 class="login-title">学生登录</h1>
      <el-form ref="LoginForm" :model="LoginForm" :rules="Rules">
        <el-form-item label="用户名" prop="UserName">
          <input v-model="LoginForm.UserName" placeholder="用户名" autofocus="" class="input">
        </el-form-item>
        <el-form-item label="密码" prop="Password">
          <input type="password" v-model="LoginForm.Password" placeholder="密码" class="input">
        </el-form-item>
        <br>
        <el-form-item>
          <a class="is-info button" @click="onSubmit">登录</a>
        </el-form-item>
        <p style="text-align: right;">
          <router-link to="/contact">忘记密码？</router-link>
        </p>
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
          } else {
            alert('error')
          }
        })
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
    created: function () {
      if (this.$cookie.get('IndexAuthenticated') === 'true') {
        this.$router.push('/')
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
</style>
