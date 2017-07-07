<template>
  <div>
    <div class="LoginForm">
      <el-row class="tac">
        <el-col :span=8 :offset=8>
          <el-form ref="LoginForm" :model="LoginForm" v-if="Authenticate===null || Authenticate===false">
            <el-form-item label="社团ID" :required=true>
              <el-input v-model="LoginForm.ClubId" placeholder="社团ID" autofocus=""></el-input>
            </el-form-item>
            <el-form-item label="密码" :required=true>
              <el-input type="password" v-model="LoginForm.Password" placeholder="密码">
              </el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="onSubmit">登陆</el-button>
            </el-form-item>
            <el-form-item>
              <p v-if="Authenticate===false">登陆失败</p>
            </el-form-item>
          </el-form>
          <p class="lead" v-if="Authenticate===true">已登录</p>
        </el-col>
      </el-row>
      <el-row class="tac" v-if="Authenticate != true">
        <el-col :span=8 :offset=8>
          <router-link to="/establish">创建社团</router-link>
        </el-col>
      </el-row>
    </div>
  </div>
</template>
<script>
  import { setCookie } from 'tiny-cookie'
  import axios from 'axios'
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
          url: 'http://127.0.0.1:8000/api/login',
          data: JSON.stringify({
            UserName: this.LoginForm.ClubId,
            Password: this.LoginForm.Password,
            UserType: 'Club'
          })
        }).then(function (response) {
          if (response.data.message === 'User Authenticated') {
            this.$store.commit('Authenticated', true)
            this.$store.commit('ApplyUserName', response.data.UserName)
            this.$store.commit('ApplyToken', response.data.Token)
            this.$router.push('/post')
          } else if (response.data.message === 'User Not Authenticated') {
            this.$store.commit('Authenticated', false)
          }
        }.bind(this)).catch(function () {
          let expireDays = 1000 * 60 * 60 * 24 * 15
          // expireDays 为有效时间
          setCookie('session', 'day', expireDays)
          // 第一个值为key，第二个为value，第三个为有限时间
          console.log('Login Failed!')
          this.$router.push('/post')
        }.bind(this))
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
  .LoginForm {
    margin-top: 13%;
  }
</style>
