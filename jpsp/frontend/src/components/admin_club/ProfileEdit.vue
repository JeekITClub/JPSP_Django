<template>
  <div>
    <el-form ref="PostForm" :model="PostForm" v-if="Authenticate===true">
      <el-form-item label="社团名称" :required="true">
        <el-input v-model="PostForm.ClubName"></el-input>
      </el-form-item>
      <el-form-item label="社团头像">
        <el-upload class="avatar-uploader" action="https://jsonplaceholder.typicode.com/posts/"
                   :show-file-list="false"
                   :on-success="handleAvatarSuccess" :before-upload="beforeAvatarUpload">
        </el-upload>
        <img v-if="imageUrl" :src="imageUrl" class="avatar">
        <i v-else class="avatar-uploader-icon
        el-icon-document"></i>
      </el-form-item>
      <el-form-item label="社长姓名" :required="true">
        <el-input v-model="PostForm.ShezhangName"></el-input>
      </el-form-item>
      <el-form-item label="社长QQ" :required="true">
        <el-input v-model="PostForm.ShezhangQQ"></el-input>
      </el-form-item>
      <el-form-item prop="PostForm.ShezhangGrade" label="社长年级" :required="true">
        <el-select v-model="PostForm.ShezhangGrade" value="">
          <el-option label="高一" value="1"></el-option>
          <el-option label="高二" value="2"></el-option>
          <el-option label="高三" value="3"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item prop="PostForm.ShezhangClass" label="社长班级" :required="true">
        <el-select v-model="PostForm.ShezhangClass" value="">
          <el-option label="1" value="1"></el-option>
          <el-option label="2" value="2"></el-option>
          <el-option label="3" value="3"></el-option>
          <el-option label="4" value="4"></el-option>
          <el-option label="5" value="5"></el-option>
          <el-option label="6" value="6"></el-option>
          <el-option label="7" value="7"></el-option>
          <el-option label="8" value="8"></el-option>
          <el-option label="9" value="9"></el-option>
          <el-option label="10" value="10"></el-option>
          <el-option label="11" value="11"></el-option>
          <el-option label="12" value="12"></el-option>
          <el-option label="13" value="13"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="是否进行招新" :required="true">
        <el-radio-group v-model="PostForm.IfRecruit">
          <el-radio :label=true>招新</el-radio>
          <el-radio :label=false>不招新</el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item label="招新QQ群" v-if="PostForm.IfRecruit">
        <el-input v-if="PostForm.IfRecruit" v-model="PostForm.QQGroup"></el-input>
      </el-form-item>
      <el-form-item label="社团邮箱" :required="true">
        <el-input v-model="PostForm.Email"></el-input>
      </el-form-item>
      <el-form-item label="社团介绍" :required="true">
        <el-input type="textarea" v-model="PostForm.Introduction"></el-input>
      </el-form-item>
      <el-form-item label="社团类型" :required="true">
        <el-checkbox-group v-model="PostForm.Label">
          <el-checkbox label="人文"></el-checkbox>
          <el-checkbox label="科技"></el-checkbox>
          <el-checkbox label="计算机"></el-checkbox>
          <el-checkbox label="摄影"></el-checkbox>
          <el-checkbox label="体育"></el-checkbox>
          <el-checkbox label="艺术"></el-checkbox>
          <el-checkbox label="学科类"></el-checkbox>
        </el-checkbox-group>
      </el-form-item>
      <el-form-item
        label="社团成就"
        v-for="(achievement, index) in PostForm.achievements"
        :label="'成就' + index"
        :key="achievements.key"
        :prop="'achievement.' + index + '.value'"
        :rules="{
      required: true, message: '不能为空', trigger: 'blur'
    }">
        <el-input v-model="achievements.value"></el-input>
        <el-button @click.prevent="removeAchievement(achievement)">删除</el-button>
      </el-form-item>
      <el-form-item>
        <el-button @click="addAchievement">新增成就</el-button>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm">提交修改</el-button>
        <el-button>取消</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>
<script>
  import axios from 'axios'
  export default {
    data () {
      return {
        PostForm: {
          ClubName: '',
          Label: [],
          Introduction: '',
          IfRecruit: true,
          QQGroup: '',
          Achievements: [
            {
              value: ''
            }
          ],
          Email: '',
          ShezhangName: '',
          ShezhangQQ: '',
          ShezhangGrade: '',
          ShezhangClass: ''
        },
        error: false,
        imageUrl: ''
      }
    },
    methods: {
      removeAchievement (item) {
        const index = this.PostForm.achievements.indexOf(item)
        if (index !== -1) {
          this.PostForm.achievements.splice(index, 1)
        }
      },
      addAchievement () {
        this.PostForm.ahievements.push({
          value: '',
          key: Date.now()
        })
      },
      submitForm () {
        axios({
          method: 'POST',
          url: 'api/club/profile/EditSubmit',
          data: {
            clubname: this.PostForm.ClubName,
            clubid: this.GetClubId,
            shezhang_name: this.PostForm.ShezhangName,
            shezhang_qq: this.PostForm.ShezhangQQ,
            shezhang_grade: this.PostForm.ShezhangGrade,
            shezhang_class: this.PostForm.ShezhangClass,
            if_recruit: this.PostForm.IfRecruit,
            enroll_group_qq: this.PostForm.QQGroup,
            email: this.PostForm.Email,
            label: this.PostForm.Label,
            introduction: this.PostForm.Introduction,
            achievements: this.PostForm.Achievements,
            // Notice Array to String
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
    computed: {
      GetClubName () {
        return this.$store.state.UserName
      },
      GetClubId () {
        return this.$store.state.ClubId
      },
      GetToken () {
        return this.$store.state.Token
      },
      Authenticate () {
        return this.$store.state.Authenticated
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
  .avatar-uploader .el-upload {
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
  }

  .avatar-uploader .el-upload:hover {
    border-color: #20a0ff;
  }

  .avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 178px;
    height: 178px;
    line-height: 178px;
    text-align: center;
  }

  .avatar {
    width: 178px;
    height: 178px;
    display: block;
  }
</style>
