<template>
  <el-form ref="RecruitClassroomApplyForm" :model="RecruitClassroomApplyForm" label-width="100%">
    <el-form-item label="公共教室需要时间" :required=true>
      <el-row>
        <el-col :span="4">
          <el-form-item prop="Date1" :required=true>
            <el-date-picker type="date" placeholder="选择日期" v-model="RecruitClassroomApplyForm.Date1"
                            style="width: 100%;"></el-date-picker>
          </el-form-item>
        </el-col>
        <el-col :span="4">
          <el-form-item prop="Date2" :required=true>
            <el-time-picker type="fixed-time" placeholder="选择开始时间" v-model="RecruitClassroomApplyForm.Date2"
                            style="width: 100%;"></el-time-picker>
          </el-form-item>
        </el-col>
        <el-col :span="4">
          <el-form-item prop="Date3" :required=true>
            <el-time-picker type="fixed-time" placeholder="选择结束时间" v-model="RecruitClassroomApplyForm.Date3"
                            style="width: 100%;"></el-time-picker>
          </el-form-item>
        </el-col>
      </el-row>
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
          if (response.data.message === 'Error') {
            this.data.error = true
          }
        }).catch(function () {
          alert('error: PostEdit')
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
