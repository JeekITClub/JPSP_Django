<template>
<div class="jpsp-basic">
  <form>
  <div class="field is-horizontal">
    <div class="field-label is-normal">
      <label class="label">用户名</label>
    </div>
    <div class="field-body">
      <div class="field">
        <p class="control is-expanded has-icons-left">
          <input class="input" type="text" v-model="ProfileForm.UserName">
          <span class="icon is-small is-left">
          <i class="fa fa-user"></i>
        </span>
        </p>
      </div>
    </div>
  </div>


  <div class="field is-horizontal">
    <div class="field-label is-normal">
      <label class="label">年级</label>
    </div>
    <div class="field-body">
      <div class="field is-narrow">
        <div class="control">
          <div class="select is-fullwidth">
            <select v-model="ProfileForm.Grade">
              <option value="1">高一</option>
              <option value="2">高二</option>
              <option value="3">高三</option>
            </select>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="field is-horizontal">
    <div class="field-label is-normal">
      <label class="label">班级</label>
    </div>
    <div class="field-body">
      <div class="field is-narrow">
        <div class="control">
          <div class="select is-fullwidth">
            <select v-model="ProfileForm.Class">
              <option value="1">1</option>
              <option value="2">2</option>
              <option value="3">3</option>
              <option value="4">4</option>
              <option value="5">5</option>
              <option value="6">6</option>
              <option value="7">7</option>
              <option value="8">8</option>
              <option value="9">9</option>
              <option value="10">10</option>
              <option value="11">11</option>
              <option value="12">12</option>
              <option value="13">13</option>
            </select>
          </div>
        </div>
      </div>
    </div>
  </div>

    <div class="field is-horizontal">
      <div class="field-label is-normal">
        <label class="label">入学年份</label>
      </div>
      <div class="field-body">
        <div class="field">
          <p class="control is-expanded">
            <input class="input" type="text" v-model="ProfileForm.AttendYear">
          </p>
        </div>
      </div>
    </div>

    <div class="field is-horizontal">
      <div class="field-label is-normal">
        <label class="label">QQ</label>
      </div>
      <div class="field-body">
        <div class="field">
          <p class="control is-expanded">
            <input class="input" type="text" v-model="ProfileForm.QQ">
          </p>
        </div>
      </div>
    </div>

    <div class="field is-horizontal">
      <div class="field-label is-normal">
        <label class="label">电子邮箱</label>
      </div>
      <div class="field-body">
        <div class="field">
          <p class="control is-expanded">
            <input class="input" type="text" v-model="ProfileForm.Email">
          </p>
        </div>
      </div>
    </div>

    <div class="field is-horizontal">
      <div class="field-label is-normal">
        <label class="label">手机号码</label>
      </div>
      <div class="field-body">
        <div class="field">
          <p class="control is-expanded">
            <input class="input" type="text" v-model="ProfileForm.Phone">
          </p>
        </div>
      </div>
    </div>


  <div class="field is-horizontal">
    <div class="field-label">
      <!-- Left empty for spacing -->
    </div>
    <div class="field-body">
      <div class="field">
        <div class="control">
          <button class="button is-primary" @click="onSubmit">
            提交
          </button>
        </div>
      </div>
    </div>
  </div>
  </form>
  </div>
</template>
<script>
  import axios from 'axios'
  export default {
    data () {
      return {
        ProfileForm: {
          UserName: '',
          Grade: '',
          Class: '',
          QQ: '',
          Email: '',
          Phone: '',
          Club: [],
          AttendYear: ''
        }
      }
    },
    computed: {
      GetUserId () {
        return this.$cookie.get('UserId')
      },
      GetIndexToken () {
        return this.$cookie.get('IndexToken')
      },
      GetUserName () {
        return this.$cookie.get('UserName')
      },
      GetIndexAuthenticated () {
        return this.$cookie.get('IndexAuthenticated')
      },
      /**
       * @return {string}
       */
      GetApi () {
        return this.$store.state.Api
      }
    },
    methods: {
      onSubmit () {
        axios({
          method: 'POST',
          url: this.GetApi + 'user/profile/submit',
          data: JSON.stringify({
            'UserId': this.GetUserId,
            'Token': this.GetIndexToken,
            'UserName': this.ProfileForm.UserName,
            'Grade': this.ProfileForm.Grade,
            'Class': this.ProfileForm.Class,
            'QQ': this.ProfileForm.QQ,
            'Email': this.ProfileForm.Email,
            'Phone': this.ProfileForm.Phone,
            'Club': this.ProfileForm.Club
          })
        }).then(function (response) {
          if (response.data.message === 'success') {
            this.ProfileForm = JSON.parse(response.data.data)
          } else {
            this.$notify.error({
              title: '错误',
              message: '无法获得数据'
            })
          }
        }.bind(this))
      },
      checkLogin () {
        if (this.$cookie.get('IndexAuthenticated') !== 'true') {
          this.$router.push('/login')
        }
      }
    },
    created () {
      this.checkLogin()
    },
    mounted: function () {
      axios({
        method: 'POST',
        url: this.GetApi + 'user/profile/get',
        data: JSON.stringify({
          UserId: this.GetUserId,
          Token: this.GetIndexToken
        })
      })
        .then(function (response) {
          if (response.data.message === 'success') {
            this.ProfileForm = JSON.parse(response.data.data)
          } else {
            this.$notify.error({
              title: '错误',
              message: '无法获得数据'
            })
          }
        }.bind(this))
    }
  }
</script>
<style scoped>
  .jpsp-basic {
    padding-top: 3%;
    padding-right: 30%;
  }
</style>
