<template>
  <div>
    <el-form :model="PostForm" :rules="rules" class="" labelPosition="right">
      <el-form-item label="联系人年级" :required=true>
        <div class="select">
          <select v-model="PostForm.LinkmanGrade">
            <option label="高一" value="1"></option>
            <option label="高二" value="2"></option>
            <option label="高三" value="3"></option>
          </select>
        </div>
        </el-form-item>
      <el-form-item label="联系人班级" :required=true>
          <div class="select">
            <select v-model="PostForm.LinkmanClass">
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
      <el-form-item label="联系人姓名" :required=true>
            <input class="input" v-model="PostForm.LinkmanName" placeholder="">
          </el-form-item>
      <el-form-item :required=true label="联系电话">
            <input v-model="PostForm.LinkmanPhoneNumber" class="input">
          </el-form-item>
      <el-form-item :required=true label="QQ">
            <input v-model="PostForm.LinkmanQq" class="input">
          </el-form-item>
      <el-form-item label="活动地点" :required=true>
        <textarea v-model="PostForm.Region" class="textarea" placeholder="请输入活动地点"></textarea>
      </el-form-item>
      <el-form-item label="活动时间" :required=true>
        <el-form-item>
          <el-date-picker v-model="PostForm.Date1" placeholder="请选择日期时间"></el-date-picker>
        </el-form-item>
      </el-form-item>
      <el-form-item label="活动内容" :required=true>
        <textarea v-model="PostForm.Content" class="textarea" placeholder=""></textarea>
      </el-form-item>
      <el-form-item label="学习过程" :required=true>
        <textarea v-model="PostForm.Process" class="textarea" placeholder=""></textarea>
      </el-form-item>
      <el-form-item label="分析评估" :required=true>
        <textarea v-model="PostForm.Assessment" class="textarea" placeholder=""></textarea>
      </el-form-item>
      <el-form-item label="活动感悟" :required=true>
        <textarea v-model="PostForm.Feeling" class="textarea" placeholder=""></textarea>
      </el-form-item>
      <el-form-item>
        <a class="button is-info" @click="submitForm">立即提交</a>
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
          ClubName: this.GetClubName,
          LinkmanGrade: '',
          LinkmanClass: '',
          LinkmanName: '',
          LinkmanPhoneNumber: '',
          LinkmanQq: '',
          Region: '',
          Date1: '',
          Content: '',
          Process: '',
          Assessment: '',
          Feeling: ''
        },
        Settings: {
          message: ''
        },
        rules: {
          ClubName: [
            {required: true, message: '请输入社团名称', trigger: 'blur'}
          ],
          Region: [
            {required: true, message: '请输入活动区域', trigger: 'blur'}
          ],
          Date1: [
            {type: 'date', required: true, message: '请选择日期', trigger: 'change'}
          ],
          Process: [
            {required: true, message: '请输入学习过程', trigger: 'change'}
          ],
          Assessment: [
            {required: true, message: '请输入分析评估', trigger: 'change'}
          ],
          Content: [
            {required: true, message: '请输入活动内容', trigger: 'change'}
          ],
          Feeling: [
            {min: 200, required: true, message: '请输入活动感受', trigger: 'change'}]
        }
      }
    },
    methods: {
      submitForm () {
        axios({
          method: 'POST',
          url: '/api/club/post/EditSubmit',
          data: JSON.stringify({
            ClubId: this.GetClubId,
            ClubName: this.GetClubName,
            Linkman: this.PostForm.Linkman,
            Region: this.PostForm.Region,
            Date1: this.PostForm.Date1,
            Content: this.PostForm.Content,
            Process: this.PostForm.Process,
            Assessment: this.PostForm.Assessment,
            Feeling: this.PostForm.Feeling,
            Token: this.GetToken
          })
        }).then(function (response) {
          if (response.data.message === 'Error') {
            this.Settings.message = 'Error'
          } else if (response.data.message === 'Success') {
            this.Settings.message = 'Success'
            this.resetForm('PostForm')
          }
        }).catch(function () {
          alert('error: PostEdit')
        })
      },
      GoToPostForm () {
        this.$router.push('/post/list')
      }
    },
    computed: {
      GetClubName () {
        return this.$cookie.get('ClubName')
      },
      GetClubId () {
        return this.$cookie.get('ClubId')
      },
      GetToken () {
        return this.$cookie.get('ClubToken')
      }
    }
  }
</script>
<style>
</style>
