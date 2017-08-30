<template>
  <div class="container establish">
    <h3 class="title is-3" align="center">创建属于自己的新社团</h3>
    <div class="field">
      <label class="label">社团名称</label>
      <div class="control">
        <input class="input" v-model="EstablishClubForm.ClubName">
      </div>
    </div>

    <div class="field">
      <label class="label">社长姓名</label>
      <div class="control">
        <input class="input" v-model="EstablishClubForm.ShezhangName">
      </div>
    </div>

    <div class="field">
      <label class="label">社长年级</label>
      <div class="control">
        <div class="select">
          <select v-model="EstablishClubForm.ShezhangGrade">
            <option value="1">高一</option>
            <option value="2">高二</option>
            <option value="3">高三</option>
          </select>
        </div>
      </div>
    </div>

    <div class="field">
      <label class="label">社长班级</label>
      <div class="control">
        <div class="select">
          <select v-model="EstablishClubForm.ShezhangClassroom">
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

    <div class="field">
      <label class="label">社长QQ号</label>
      <div class="control">
        <input class="input" type="number" v-model="EstablishClubForm.ShezhangQQ">
      </div>
    </div>

    <div class="field">
      <label class="label">是否招新</label>
      <div class="control">
        <label class="checkbox">
          <input type="checkbox" v-model="EstablishClubForm.IfRecruit">
          是否招新
        </label>
      </div>
    </div>

    <div class="field" v-if="EstablishClubForm.IfRecruit">
      <label class="label">招新QQ群</label>
      <div class="control">
        <input class="input" type="number" v-model="EstablishClubForm.QQGroup">
      </div>
    </div>

    <!--<div class="field">-->
    <!--<label class="label">社团邮箱</label>-->
    <!--<div class="control">-->
    <!--<input class="input" type="text" v-model="EstablishClubForm.Email">-->
    <!--</div>-->
    <!--</div>-->

    <div class="field">
      <label class="label">社团简介</label>
      <div class="control">
        <textarea class="textarea" v-model="EstablishClubForm.Introduction"></textarea>
      </div>
    </div>

    <div class="field">
      <div class="control">
        <button class="button is-primary" @click="submitForm">提交审核</button>
        <hr>
        <p align="center">提交审核后需要社团部批准方可开始招新</p>
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
        EstablishClubForm: {
          ClubName: '',
          ShezhangName: '',
          ShezhangQQ: '',
          ShezhangGrade: '',
          ShezhangClassroom: '',
          Introduction: '',
          IfRecruit: true,
          QQGroup: '',
          Email: ''
        }
      }
    },
    methods: {
      submitForm () {
        axios({
          method: 'POST',
          url: this.GetApi + 'club',
          data: Qs.stringify({
            Clubname: this.EstablishClubForm.ClubName,
            Shezhang_Name: this.EstablishClubForm.ShezhangName,
            Shezhang_QQ: this.EstablishClubForm.ShezhangQQ,
            Shezhang_Grade: this.EstablishClubForm.ShezhangGrade,
            Shezhang_Classroom: this.EstablishClubForm.ShezhangClassroom,
            Introduction: this.EstablishClubForm.Introduction,
            IfRecruit: this.EstablishClubForm.IfRecruit,
            QQGroup: this.EstablishClubForm.QQGroup,
            Email: this.EstablishClubForm.Email
          }),
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
          }
        }).then(function (response) {
          if (response.data.message === 'success') {
            this.$router.push('/')
            this.$notify({
              title: '成功',
              message: '成功创建社团',
              type: 'success'
            })
          }
          if (response.data.message === 'error') {
            this.$notify.error({
              title: '错误',
              message: '无法创建社团'
            })
          }
        }.bind(this)).catch(function () {
          this.$notify.error({
            title: '错误',
            message: '无法创建社团'
          })
        })
      },
      checkLogin () {
        if (this.$cookie.get('IndexAuthenticated') !== 'true') {
          this.$router.push('/login')
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
    created () {
      this.checkLogin()
    }
  }
</script>
<style scoped>
  .establish {
    padding-top: 50px;
    padding-left: 150px;
    padding-right: 150px;
    padding-bottom: 50px;
  }
</style>
