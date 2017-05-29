<template>
  <div>
    <div class="LoginForm">
      <el-row class="tac pic">
        <el-col :span="8" offset="8">
          <el-form ref="form" :model="form">
            <el-form-item label="社团ID" required="true">
              <el-input v-model="LoginForm.Clubid" placeholder="社团ID" autofocus=""></el-input>
            </el-form-item>
            <el-form-item label="密码" required="true">
              <el-input v-model="LoginForm.Password" placeholder="密码">
              </el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="onSubmit">登陆</el-button>
            </el-form-item>
            <el-form-item>
              <a v-if="error===false">登陆失败</a>
            </el-form-item>
          </el-form>
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
          Clubid: '',
          Password: ''
        }
      }
    },
    methods: {
      onSubmit () {
        console.log('submit!')
        axios({
          method: 'POST',
          url: '../api/login/',
          data: {
            UserName: this.LoginForm.Clubid,
            Password: this.LoginForm.Password,
            error: false
          }
        })
          .then(function (response) {
            if (response.data.message === 'User Authenticated') {
              console.log('success!!!')
              this.store.commit('Login_in')
            } else if (response.data.message === 'User Not Authenticated') {
              console.log('success!')
              this.error = true
            }
          })
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
