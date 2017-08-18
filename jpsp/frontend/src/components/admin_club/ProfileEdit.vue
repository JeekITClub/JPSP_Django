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
      <el-form-item label="社团邮箱" :required="true">
        <input type="email" v-model="ProfileForm.Email" class="input">
      </el-form-item>
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
          Email: '',
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
          method: 'POST',
          url: 'api/club/profile/EditSubmit',
          data: {
            clubname: this.ProfileForm.ClubName,
            clubid: this.GetClubId,
            shezhang_name: this.ProfileForm.ShezhangName,
            shezhang_qq: this.ProfileForm.ShezhangQQ,
            shezhang_grade: this.ProfileForm.ShezhangGrade,
            shezhang_class: this.ProfileForm.ShezhangClass,
            if_recruit: this.ProfileForm.IfRecruit,
            enroll_group_qq: this.ProfileForm.QQGroup,
            email: this.ProfileForm.Email,
            label: this.ProfileForm.Label,
            introduction: this.ProfileForm.Introduction,
            achievements: this.ProfileForm.Achievements,
            Token: this.GetToken
          }
        }).then(function (response) {
          if (response.data.message === 'error') {
            this.error = true
          } else {
            alert('success')
          }
        }.bind(this)).catch(function () {
          alert('error: ProfileEdit')
        })
      },
      handleAvatarSuccess (res, file) {
        this.imageUrl = URL.createObjectURL(file.raw)
      },
      beforeAvatarUpload (file) {
        const isJPG = file.type === 'image/jpeg'
        const isLt2M = file.size / 1024 / 1024 < 2

        if (!isJPG) {
          this.$message.error('上传头像图片只能是 JPG 格式!')
        }
        if (!isLt2M) {
          this.$message.error('上传头像图片大小不能超过 2MB!')
        }
        return isJPG && isLt2M
      }
    },
    mounted: function () {
      axios({
        method: 'POST',
        url: 'http://127.0.0.1:8000/api/club/profile/get',
        data: JSON.stringify({
          ClubId: this.GetClubId,
          Token: this.GetToken
        })
      })
        .then(function (response) {
          if (response.data.message === 'success') {
            var profile = JSON.parse(response.data.data)
            console.log('success')
            this.PostForm.ClubName = profile
          } else {
            console.log('error')
          }
        }.bind(this))
    }
  }
</script>
<style>
</style>
