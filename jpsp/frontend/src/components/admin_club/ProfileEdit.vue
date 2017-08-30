<template>
  <div>
    <el-form ref="ProfileForm" :model="ProfileForm">
      <el-form-item label="社团名称" :required="true" prop="ClubName">
        <input v-model="ProfileForm.ClubName" class="input is-primary">
      </el-form-item>
      <el-form-item label="社团类型" :required="true">
        <div class="select">
          <select v-model="ProfileForm.Type">
            <option value="1">自立精神</option>
            <option value="2">共生意识</option>
            <option value="3">科学态度</option>
            <option value="4">人文情怀</option>
            <option value="5">领袖气质</option>
          </select>
        </div>
      </el-form-item>
      <el-form-item label="社长姓名" :required="true" prop="ShezhangName">
        <input v-model="ProfileForm.ShezhangName" class="input">
      </el-form-item>
      <el-form-item label="社长QQ" :required="true" prop="ShezhangQQ">
        <input v-model="ProfileForm.ShezhangQQ" class="input">
      </el-form-item>
      <el-form-item prop="ShezhangGrade" label="社长年级" :required="true">
        <div class="select">
          <select v-model="ProfileForm.ShezhangGrade">
            <option value="1">高一</option>
            <option value="2">高二</option>
            <option value="3">高三</option>
          </select>
        </div>
      </el-form-item>
      <el-form-item prop="ShezhangClass" label="社长班级" :required="true">
        <div class="select">
          <select v-model="ProfileForm.ShezhangClass">
            <option label="1" value="1"></option>
            <option label="2" value="2"></option>
            <option label="3" value="3"></option>
            <option label="4" value="4"></option>
            <option label="5" value="5"></option>
            <option label="6" value="6"></option>
            <option label="7" value="7"></option>
            <option label="8" value="8"></option>
            <option label="9" value="9"></option>
            <option label="10" value="10"></option>
            <option label="11" value="11"></option>
            <option label="12" value="12"></option>
            <option label="13" value="13"></option>
          </select>
        </div>
      </el-form-item>
      <el-form-item label="是否进行招新" :required="true">
        <div class="control">
          <label class="radio">
            <input type="radio" v-model="ProfileForm.IfRecruit" value="true">招新
          </label>
          <label class="radio">
            <input type="radio" v-model="ProfileForm.IfRecruit" value="false">不招新
          </label>
        </div>
      </el-form-item>
      <el-form-item label="招新QQ群" v-if="ProfileForm.IfRecruit">
        <input v-if="ProfileForm.IfRecruit" v-model="ProfileForm.QQGroup" class="input">
      </el-form-item>
      <!--<el-form-item label="社团邮箱" :required="true">-->
      <!--<input type="email" v-model="ProfileForm.Email" class="input">-->
      <!--</el-form-item>-->
      <el-form-item label="社团介绍" :required="true">
        <textarea class="textarea" v-model="ProfileForm.Introduction"></textarea>
      </el-form-item>

      <el-form-item>
        <a class="button is-info" @click="submitForm">提交修改</a>
      </el-form-item>
    </el-form>
  </div>
</template>
<script>
  import Qs from 'qs'
  import axios from 'axios'

  export default {
    data () {
      return {
        ProfileForm: {
          ClubName: '',
          Introduction: '',
          IfRecruit: true,
          QQGroup: '',
          Achievements: '',
//          Email: '',
          ShezhangName: '',
          ShezhangQQ: '',
          ShezhangGrade: '',
          ShezhangClass: '',
          Type: ''
        }
      }
    },
    methods: {
      submitForm () {
        axios({
          method: 'PUT',
          url: this.GetApi + 'clubs/profile',
          data: Qs.stringify({
            ClubName: this.ProfileForm.ClubName,
            ClubId: this.GetClubId,
            ShezhangName: this.ProfileForm.ShezhangName,
            ShezhangQQ: this.ProfileForm.ShezhangQQ,
            ShezhangGrade: this.ProfileForm.ShezhangGrade,
            ShezhangClass: this.ProfileForm.ShezhangClass,
            IfRecruit: this.ProfileForm.IfRecruit,
            QQGroup: this.ProfileForm.QQGroup,
            Email: this.ProfileForm.Email,
            Introduction: this.ProfileForm.Introduction,
            Achievements: this.ProfileForm.Achievements,
            Token: this.GetClubToken
          }),
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
          }
        })
          .then(function (response) {
            if (response.message === 'error') {
              this.$notify.error({
                'message': 'error',
                'title': 'error'
              })
            } else if (response.message === 'success') {
              this.$notify.success({
                'message': 'success',
                'title': 'success'
              })
            }
          }.bind(this))
      }
    },
    mounted: function () {
      axios({
        method: 'GET',
        url: this.GetApi + 'clubs/profile',
        params: {
          ClubId: this.GetClubId
        }
      })
        .then(function (response) {
          if (response.data.message === 'success') {
            this.ProfileForm = response.data.data
          } else {
            this.$notify.error({
              'title': 'error',
              'message': 'error'
            })
          }
        }.bind(this))
        .catch(function (err) {
          console.log(err)
          this.$notify.error({
            'title': 'error',
            'message': 'error'
          })
        })
    },
    computed: {
      GetClubId () {
        return this.$cookie.get('ClubId')
      },
      GetToken () {
        return this.$cookie.get('ClubToken')
      },
      /**
       * @return {string}
       */
      GetApi () {
        return this.$store.state.Api
      }
    }
  }
</script>
<style>
</style>
