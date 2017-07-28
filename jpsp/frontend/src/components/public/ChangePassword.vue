<template>
  <div>
    <el-row>
      <el-col :span="8" :offset="8">
        <el-form :ref="ChangePasswordForm" :model="ChangePasswordForm" :rule="Rule">
          <el-form-item label="原密码">
            <el-input v-model="ChangePasswordForm.OriginalPassword" placeholder="" type="password"></el-input>
          </el-form-item>
          <el-form-item label="新密码">
            <el-input v-model="ChangePasswordForm.NewPassword" placeholder="" type="password"></el-input>
          </el-form-item>
          <el-form-item label="确定新密码">
            <el-input v-model="ChangePasswordForm" placeholder="" type="password"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button @click="submitForm" type="primary">提交修改</el-button>
          </el-form-item>
        </el-form>
      </el-col>
    </el-row>
  </div>
</template>
<script>
  import axios from 'axios'
  export default {
    data () {
      var validatePass = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请输入密码'))
        } else {
          if (this.ChangePasswordForm.NewPassword !== '') {
            this.$refs.ChangePasswordForm.validateField('checkPass')
          }
          callback()
        }
      }
      var validatePass2 = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请再次输入密码'))
        } else if (value !== this.ChangePasswordForm.Password) {
          callback(new Error('两次输入密码不一致!'))
        } else {
          callback()
        }
      }
      return {
        ChangePasswordForm: {
          OriginalPassword: '',
          NewPassword: '',
          ConfirmNewPassword: ''
        },
        Rule: {
          pass: [
            {vaildator: validatePass, trigger: 'blur'}
          ],
          checkPass: [
            {vaildator: validatePass2, trigger: 'blur'}
          ]
        }
      }
    },
    methods: {
      submitForm () {
        this.$refs['ChangePasswordForm'].vaildate((vaild) => {
          if (vaild) {
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
          } else {
            this.$notify.error({
              'title': '错误',
              'message': '无法更改密码'
            })
          }
        })
      }
    }
  }
</script>
<style>
</style>
