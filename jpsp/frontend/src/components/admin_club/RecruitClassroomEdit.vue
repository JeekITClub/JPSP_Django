<template>
  <el-form ref="RecruitClassroomApplyForm" :model="RecruitClassroomApplyForm">
    <p class="lead">公共教室申请</p>
    <el-form-item label="开始时间" prop="Date1" :required=true>
      <el-date-picker type="datetime" placeholder="选择日期" v-model="RecruitClassroomApplyForm.Date1"
      ></el-date-picker>
    </el-form-item>
    <el-form-item label="结束时间" prop="Date2" :required=true>
      <el-date-picker type="datetime" placeholder="选择开始时间"
                      v-model="RecruitClassroomApplyForm.Date2"></el-date-picker>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="submitForm">提交</el-button>
    </el-form-item>
  </el-form>
</template>
<script>
  import axios from 'axios'
  export default {
    name: 'RecruitClassroomApply',
    data () {
      return {
        RecruitClassroomApplyForm: {
          ClubName: this.GetClubName,
          Date1: '',
          Date2: '',
          Date3: ''
        },
        error: false
      }
    },
    methods: {
      submitForm () {
        axios({
          method: 'POST',
          url: '',
          data: JSON.stringify({
            ClubId: this.GetClubId,
            ClubName: this.GetClubName,
            Date1: this.RecruitClassroomApplyForm.Date1,
            Date2: this.RecruitClassroomApplyForm.Date2,
            Date3: this.RecruitClassroomApplyForm.Date3,
            Token: this.GetToken
          })
        }).then(function (response) {
          if (response.data.message === 'success') {
            console.log('success')
          }
          if (response.data.message === 'error') {
            console.log('error')
          }
        }).catch(function () {
          console.log('error')
        })
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
    }
  }
</script>
<style>
</style>
