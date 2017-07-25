<template>
  <div>
    <el-form :ref="ChangePasswordForm" :model="ChangePasswordForm">
      <el-form-item label="原密码">
        <el-input v-model="ChangePasswordForm.OriginalPassword" placeholder="请输入原密码"></el-input>
      </el-form-item>
    </el-form>
    <el-form-item label="新密码">
      <el-input v-model="ChangePasswordForm.NewPassword" placeholder="请输入新密码"></el-input>
    </el-form-item>
    <el-form-item label="确定新密码">
      <el-input v-model="ChangePasswordForm" placeholder="重复新密码"></el-input>
    </el-form-item>
    <el-form-item>
      <el-button @click="submitForm" type="primary">提交修改</el-button>
    </el-form-item>
  </div>
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
          data: {}
        }).then(function (response) {
          if (response.data.message === 'success') {
            this.$notify({
              title: '成功',
              message: '成功更改密码',
              type: 'success'
            })
          }
          if (response.data.message === 'error') {
            this.$notify.error({
              'title': '错误',
              'message': '无法更改密码'
            })
          }
        }.bind(this)).catch(function () {
          this.$notify.error({
            'title': '错误',
            'message': '无法更改密码'
          })
        })
      }
    }
  }
</script>
<style>
</style>
