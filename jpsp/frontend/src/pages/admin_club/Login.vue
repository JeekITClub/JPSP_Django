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
  import { setCookie } from 'tiny-cookie'
  import axios from 'axios'
  import ElForm from '../../../node_modules/element-ui/packages/form/src/form'
  export default {
    components: {ElForm},
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
