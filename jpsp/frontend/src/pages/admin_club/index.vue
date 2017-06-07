<template>
  <div>
    <div class="LoginForm">
      <el-row class="tac">
        <el-col :span="8" :offset="8">
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
          <h1 v-if="Authenticate===true">已登录</h1>
        </el-col>
      </el-row>
      <!--<el-row class="tac">-->
      <!--<el-col :span="8" offset="8">-->
      <!--<router-link to="EstablishClub">创建社团</router-link>-->
      <!--</el-col>-->
      <!--</el-row>-->
    </div>
  </div>
</template>
<script>
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
          url: '',
          data: JSON.stringify({
            UserName: this.LoginForm.ClubId,
            Password: this.LoginForm.Password
          })
        }).then(function (response) {
          if (response.data.message === 'User Authenticated') {
            this.$store.commit('Authenticate')
            this.$store.commit('ApplyUserName', this.UserName)
          } else if (response.data.message === 'User Not Authenticated') {
            this.data.settings.NotAuthenticated = true
          }
        })
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
  .LoginForm {
    margin-top: 13%;
  }
</style>
