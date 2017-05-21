<template>
  <div>
    <el-row class="tac">
      <el-col :span="8" offset="8">
        <el-form ref="form" :model="form">
          <el-form-item label="用户名" required="true">
            <el-input v-model="form.username" placeholder="用户名" autofocus=""></el-input>
          </el-form-item>
          <el-form-item label="密码" required="true">
            <el-input v-model="form.password" placeholder="密码">
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
        form: {
          name: '',
          password: ''
        }
      }
    },
    methods: {
      onSubmit () {
        console.log('submit!')
        axios({
          method: 'POST',
          url: 'api/club/login/',
          data:{
              name: this.form.name,
              password: this.form.password
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
