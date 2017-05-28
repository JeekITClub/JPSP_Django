<template>
  <div>
    <el-row class="tac">
      <el-col :span="8" offset="8">
        <el-form ref="form" :model="form">
          <el-form-item label="社团ID" required="true">
            <el-input v-model="LoginForm.Clubid" placeholder="社团ID" autofocus=""></el-input>
          </el-form-item>
          <el-form-item label="密码" required="true">
            <el-input v-model="LoginForm.password" placeholder="密码">
            </el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="onSubmit">登陆</el-button>
          </el-form-item>
        </el-form>
      </el-col>
    </el-row>
    <router-link to="EstablishClub">创建社团</router-link>
    <JFooter></JFooter>
  </div>
</template>
<script>
  import axios from 'axios'
  import JFooter from '../../components/public/JFooter.vue'
  export default {
    components: {
      'JFooter': JFooter
    },
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
          url: 'api/club/login/',
          data: {
            name: this.LoginForm.Clubname,
            password: this.LoginForm.Password
          }
        })
          .then(function (response) {
            console.log(response)
          })
          .catch(function (error) {
            console.log(error)
          })
      }
    }
  }
</script>
<style>
  @import url("//unpkg.com/element-ui@1.3.2/lib/theme-default/index.css");
</style>
