<template>
  <div>

    <el-row :gutter=20>
      <el-col :span="4">
        <club_aside></club_aside>
      </el-col>
      <el-col :span=20 v-if="Authenticate===true">
        <el-form :model="PostForm" :rules="rules" class="" labelPosition="right">
          <el-form-item label="活动联系人" :required=true>
            <el-col :span=4>
              <el-form-item :prop="LinkmanGrade">
                <el-select v-model="PostForm.LinkmanGrade" placeholder="请选择年级" value="">
                  <el-option label="高一" value="1"></el-option>
                  <el-option label="高二" value="2"></el-option>
                  <el-option label="高三" value="3"></el-option>
                </el-select>
              </el-form-item>
            </el-col>
            <el-col :span=4>
              <el-form-item :prop="LinkmanClass">
                <el-select v-model="PostForm.LinkmanClass" placeholder="请选择班级" value="">
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
            </el-col>
            <el-col :span=4>
              <el-form-item :prop="LinkmanName">
                <el-input v-model="PostForm.LinkmanName" placeholder="请填写姓名"></el-input>
              </el-form-item>
            </el-col>
            <el-col :span=4>
              <el-form-item :prop="LinkmanPhoneNumber" :required=true>
                <el-input v-model="PostForm.LinkmanPhoneNumber" placeholder="请填写联系电话"></el-input>
              </el-form-item>
            </el-col>
            <el-col :span=4>
              <el-form-item :prop="LinkmanQq" :required=true>
                <el-input v-model="PostForm.LinkmanQq" placeholder="请填写QQ"></el-input>
              </el-form-item>
            </el-col>
          </el-form-item>
          <el-col :span=20>
            <el-form-item label="活动地点" :prop="Region" :required=true>
              <el-input v-model="PostForm.Region"></el-input>
            </el-form-item>
          </el-col>
          <el-form-item label="活动时间" :required=true>
            <el-form-item :prop="Date1">
              <el-date-picker
                v-model="PostForm.Date1"
                type="datetime"
                placeholder="选择日期时间">
              </el-date-picker>
            </el-form-item>
          </el-form-item>
          <el-form-item label="活动内容" :prop="Content" :required=true>
            <el-input type="textarea" v-model="PostForm.Content"></el-input>
          </el-form-item>
          <el-form-item label="学习过程" :prop="Process" :required=true>
            <el-input type="textarea" v-model="PostForm.Process"></el-input>
          </el-form-item>
          <el-form-item label="分析评估" :prop="Assessment" :required=true>
            <el-input type="textarea" v-model="PostForm.Assessment"></el-input>
          </el-form-item>
          <el-form-item label="活动感悟" :prop="Feeling" :required=true>
            <el-input type="textarea" v-model="PostForm.Feeling"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="submitForm">立即提交</el-button>
          </el-form-item>
        </el-form>
        <el-row>
          <el-col span="6" offset="18">
            <a v-if="Settings.message==='Error'">提交失败！请重新填写或联系管理员</a>
            <a v-if="Settings.message==='Success'">提交成功</a>
          </el-col>
        </el-row>
      </el-col>
      <el-col :span=20 v-if="Authenticate===false || Authenticate===null">
        <p>未登陆</p>
      </el-col>
    </el-row>
  </div>
</template>
<script>
  import axios from 'axios'
  import JAside from '../../components/admin_club/ClubAside.vue'
  export default {
    components: {
      'club_aside': JAside
    },
    data () {
      return {
        PostForm: {
          ClubName: this.GetClubName,
          LinkmanGrade: '',
          LinkmanClass: '',
          LinkmanName: '',
          LinkmanPhoneNumber: '',
          LinkmaanQq: '',
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
      resetForm (formName) {
        this.$refs[formName].resetFields()
      }
    },
    computed: {
      Authenticate () {
        return this.$store.state.Authenticated
      },
      GetClubName () {
        return this.$store.state.UserName
      },
      GetClubId () {
        return this.$store.state.ClubId
      },
      GetToken () {
        return this.$store.state.Token
      }
    }
  }
</script>
<style>
</style>
