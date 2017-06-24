<template>
  <div class="LoginForm">
    <el-row class="tac">
      <el-col :span="8" :offset="8">
        <el-form ref="LoginForm" :model="LoginForm" v-if="Authenticate===false || Authenticate===null">
          <el-form-item label="社团部账号" :required=true>
            <el-input v-model="LoginForm.UserName" placeholder="社团部账号" autofocus=""></el-input>
          </el-form-item>
          <el-form-item label="密码" :required=true>
            <el-input type="password" v-model="LoginForm.Password" placeholder="密码">
            </el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="onSubmit">登陆</el-button>
          </el-form-item>
          <el-form-item>
            <p v-if="Authenticate===true">登陆失败</p>
          </el-form-item>
        </el-form>
        <h1 v-if="Authenticate===true">已登录</h1>
      </el-col>
    </el-row>
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
    },
    computed: {
      Authenticate () {
        return this.$store.state.Authenticated
      }
    }
  }
</script>
<style>
</style>
