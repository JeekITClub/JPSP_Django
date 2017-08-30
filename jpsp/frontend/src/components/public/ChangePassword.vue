<template>
  <div>
    <el-form :ref="ChangePasswordForm" :model="ChangePasswordForm" :rule="Rule">
      <el-form-item label="原密码">
        <input v-model="ChangePasswordForm.OriginalPassword" placeholder="" type="password" class="input">
      </el-form-item>
      <el-form-item label="新密码">
        <input v-model="ChangePasswordForm.NewPassword" placeholder="" type="password" class="input">
      </el-form-item>
      <el-form-item label="确认新密码">
        <input v-model="ChangePasswordForm.ConfirmNewPassword" placeholder="" type="password" class="input">
      </el-form-item>
      <el-form-item>
        <el-button @click="submitForm" type="primary">提交修改</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>
<script>
  import axios from 'axios'
  import Qs from 'qs'

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
        if (this.OriginalPassword === this.NewPassword) {
          this.$notify.error({
            title: '错误',
            message: '新密码与原密码相同'
          })
        } else if (this.NewPassword !== this.ConfirmNewPassword) {
          this.$notify.error({
            title: '错误',
            message: '确认密码与新密码不同'
          })
        } else {
          axios({
            method: 'PUT',
            url: this.GetApi + 'users/password',
            data: Qs.stringfy({
              UserId: this.GetUserId,
              Password: this.NewPassword
            }),
            headers: {
              'Content-Type': 'application/x-www-form-urlencoded'
            }
          })
            .then(function (response) {
              if (response.data.message === 'success') {
                this.$notify({
                  title: '成功',
                  message: '成功更改密码',
                  type: 'success'
                })
              }
              if (response.data.message === 'error') {
                this.$notify.error({
                  title: '错误',
                  message: '无法更改密码'
                })
              }
            }.bind(this))
            .catch(function () {
              this.$notify.error({
                'title': '错误',
                'message': '无法更改密码'
              })
            }.bind(this))
        }
      }
    },
    computed: {
      GetApi () {
        return this.$store.state.Api
      }
    }
  }
</script>
<style>
</style>
