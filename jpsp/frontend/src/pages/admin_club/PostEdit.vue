<template>
  <div>
    <el-row :gutter="20">
      <el-col :span="4">
        <club_aside></club_aside>
      </el-col>
      <el-col :span="20">
        <el-form :model="PostForm" :rules="rules" class="" labelPosition="right">
          <el-form-item label="社团名称" prop="ClubName">
            <el-input v-model="PostForm.ClubName" autofocus=""></el-input>
          </el-form-item>
          <el-form-item label="活动联系人" required="">
            <el-col :span="4">
              <el-form-item prop="Linkman.Grade">
                <el-select v-model="PostForm.Linkman.Grade" placeholder="请选择年级" value="">
                  <el-option label="高一" value="1"></el-option>
                  <el-option label="高二" value="2"></el-option>
                  <el-option label="高三" value="3"></el-option>
                </el-select>
              </el-form-item>
            </el-col>
            <el-col :span="4">
              <el-form-item prop="Linkman.Class">
                <el-select v-model="PostForm.Linkman.Class" placeholder="请选择班级" value="">
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
            <el-col :span="4">
              <el-form-item prop="Linkman.Name">
                <el-input v-model="PostForm.Linkman.Name" placeholder="请填写姓名"></el-input>
              </el-form-item>
            </el-col>
            <el-col :span="4">
              <el-form-item prop="Linkman.PhoneNumber">
                <el-input v-model="PostForm.Linkman.PhoneNumber" placeholder="请填写联系电话"></el-input>
              </el-form-item>
            </el-col>
            <el-col :span="4">
              <el-form-item prop="Linkman.Qq">
                <el-input v-model="PostForm.Linkman.Qq" placeholder="请填写QQ"></el-input>
              </el-form-item>
            </el-col>
          </el-form-item>
          <el-form-item label="活动地点" prop="Region">
            <el-input v-model="PostForm.region"></el-input>
          </el-form-item>
          <el-form-item label="活动时间" required>
            <el-col :span="4">
              <el-form-item prop="Date1">
                <el-date-picker type="date" placeholder="选择日期" v-model="PostForm.Date1"
                                style="width: 100%;"></el-date-picker>
              </el-form-item>
            </el-col>
            <el-col class="line" :span="4"></el-col>
            <el-col :span="4">
              <el-form-item prop="date2">
                <el-time-picker type="fixed-time" placeholder="选择时间" v-model="PostForm.Date2"
                                style="width: 100%;"></el-time-picker>
              </el-form-item>
            </el-col>
          </el-form-item>
          <el-form-item label="活动内容" prop="Content">
            <el-input type="textarea" v-model="PostForm.Content"></el-input>
          </el-form-item>
          <el-form-item label="学习过程" prop="Process">
            <el-input type="textarea" v-model="PostForm.Process"></el-input>
          </el-form-item>
          <el-form-item label="分析评估" prop="Assessment">
            <el-input type="textarea" v-model="PostForm.Assessment"></el-input>
          </el-form-item>
          <el-form-item label="活动感悟" prop="Feeling">
            <el-input type="textarea" v-model="PostForm.Feeling"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="submitForm('PostForm')">立即提交</el-button>
          </el-form-item>
        </el-form>
      </el-col>
    </el-row>
  </div>
</template>
<script>
  import axios from 'axios'
  import JAside from '../../components/admin_club/ClubAside.vue'
  export default {
    name: 'PostEdit',
    components: {
      'club_aside': JAside
    },
    data () {
      return {
        PostForm: {
          ClubName: this.$store.state.ClubName,
          Linkman: {
            Grade: '',
            Class: '',
            Name: '',
            PhoneNumber: '',
            Qq: ''
          },
          Region: '',
          Date1: '',
          Date2: '',
          Content: '',
          Process: '',
          Assessment: '',
          Feeling: ''
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
          Date2: [
            {type: 'date', required: true, message: '请选择时间', trigger: 'change'}
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
            ClubId: this.$store.state.ClubId,
            ClubName: this.PostForm.ClubName,
            Linkman: this.PostForm.Linkman,
            Region: this.PostForm.Region,
            Date1: this.PostForm.Date1,
            Date2: this.PostForm.Date2,
            Content: this.PostForm.Content,
            Process: this.PostForm.Process,
            Assessment: this.PostForm.Assessment,
            Feeling: this.PostForm.Feeling,
            Token: this.$store.state.Token
          })
        }).then(function (response) {
          alert(JSON.stringify(response.data))
        }).catch(function () {
          alert('error')
        })
      },
      resetForm (formName) {
        this.$refs[formName].resetFields()
      }
    }
  }
</script>
<style>
</style>
