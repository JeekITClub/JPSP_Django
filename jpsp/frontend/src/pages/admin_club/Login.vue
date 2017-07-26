<template>
  <div>
    <div class="LoginForm">
      <el-row class="tac">
        <el-col :span=8 :offset=8>
          <el-form ref="LoginForm" :model="LoginForm">
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
          </el-form>
        </el-col>
      </el-row>
    </div>
  </div>
</template>
<script>
  import {setCookie} from 'tiny-cookie'
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
            let expireDays = 1000 * 60 * 60 * 24 * 3
            // this.$store.commit('ApplyUserName', response.data.UserName)
            setCookie('ClubId', this.LoginForm.ClubId, expireDays)
            setCookie('Clubname', response.data.Clubname, expireDays)
            // this.$store.commit('ApplyToken', response.data.Token)
            setCookie('Token', response.data.Token, expireDays)
            // expireDays 为有效时间
            setCookie('ClubAuthenticated', true, expireDays)
            // 第一个值为key，第二个为value，第三个为有限时间
            this.$router.push('/dashboard')
          } else {
            console.log('error')
          }
        }.bind(this))
      }
    }
  }
</script>
<style>
  .LoginForm {
    margin-top: 13%;
  }
</style>
