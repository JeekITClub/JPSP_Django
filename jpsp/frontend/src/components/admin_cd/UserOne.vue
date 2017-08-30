<template>
  <div>
    <h2 class="title is-3">新建单独学生用户</h2>
    <hr>
    <div class="field">
      <label class="label">姓名</label>
      <div class="control">
        <input class="input" placeholder="">
      </div>
    </div>
    <div class="field">
      <label class="label">班级</label>
      <div class="control">
        <input class="input" type="number" placeholder="">
      </div>
    </div>
    <div class="field">
      <label class="label">年级</label>
      <div class="control">
        <input class="input" type="number" placeholder="">
      </div>
    </div>
    <div class="field">
      <label class="label">QQ</label>
      <div class="control">
        <input class="input" type="number" placeholder="">
      </div>
    </div>
    <div class="field">
      <label class="label">用户ID</label>
      <div class="control">
        <input class="input" type="number" placeholder="20170101">
      </div>
    </div>
    <div class="field">
      <label class="label">密码</label>
      <div class="control">
        <input class="input" type="password" placeholder="">
      </div>
    </div>
  </div>
</template>
<script>
  import axios from 'axios'
  import Qs from 'qs'
  export default {
    data () {
      return {
        Name: '',
        Grade: null,
        Class: null,
        QQ: null,
        UserId: null,
        Password: null
      }
    },
    computed: {
      /**
       * @return {string}
       */
      GetApi () {
        return this.$store.state.Api
      },
      GetCDToken () {
        return this.$cookie.get('CDToken')
      },
      GetUserId () {
        return this.$cookie.get('CDUserId')
      }
    },
    methods: {
      onSubmit () {
        axios({
          method: 'POST',
          url: this.GetApi + 'users/profile',
          data: Qs.stringify({
            UserName: this.Name,
            Grade: this.Grade,
            Class: this.Class,
            QQ: this.QQ,
            Password: this.Password,
            UserId: this.UserId,
            Token: this.GetCDToken,
            CDUserId: this.GetUserId
          }),
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
          }
        })
          .then(function (response) {
            if (response.data.message === 'success') {
              this.$notify.success({
                title: '成功',
                message: '创建成功'
              })
            } else {
              this.$notify.error({
                title: '错误',
                message: '创建失败'
              })
            }
          }.bind(this))
          .catch(function () {
            this.$notify.error({
              title: '错误',
              message: '创建失败'
            })
          })
      }
    }
  }
</script>
<style>
</style>
