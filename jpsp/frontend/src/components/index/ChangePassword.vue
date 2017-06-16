<template>
  <el-form :ref="ChangePasswordForm" :model="ChangePasswordForm">
<el-form-item label="原密码">
<el-input v-model="ChangePasswordForm.OriginalPassword" placeholder="请输入原密码"></el-input></el-form-item>
  </el-form>
  <el-form-item label="新密码">
  <el-input v-model="ChangePasswordForm.NewPassword" placeholder="请输入新密码"></el-input>
</el-form-item>
<el-form-item label="确定新密码">
<el-input v-model="ChangePasswordForm" placeholder="重复新密码"></el-input></el-form-item>
<el-form-item>
<el-button @click="submitForm" type="primary">提交修改</el-button>
</el-form-item>
</template>
<script>
import axios from 'axios'
  export default {
    data () {
      return {
          ChangePasswordForm: {
              OriginalPassword: '',
              NewPassword: '',
              ConfirmNewPassword: ''
          }
      }
  },
  methods: {
      submitForm () {
          axios({
              method: 'POST',
              url: 'api/index/profile/ChangePassword',
              data : {
                 
              }
          })
      }
  }
  }
</script>
<style>
</style>
