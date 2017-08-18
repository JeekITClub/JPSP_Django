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
  // TODO: 公共教室两个时间的验证 后一个时间不能比前一个早 而且不能超过一天的周期
  import { getCookie } from 'tiny-cookie'
  import axios from 'axios'
  export default {
    name: 'RecruitClassroomApply',
    data () {
      return {
        RecruitClassroomApplyForm: {
          Date1: '',
          Date2: ''
        }
      }
    },
    methods: {
      submitForm () {
        axios({
          method: 'POST',
          url: '',
          data: JSON.stringify({
            ClubId: this.GetClubId,
            Date1: this.RecruitClassroomApplyForm.Date1,
            Date2: this.RecruitClassroomApplyForm.Date2,
            Token: this.GetClubToken
          })
        }).then(function (response) {
          if (response.data.message === 'success') {
            this.$notify({
              'title': '成功',
              'message': '成功申请公共教室',
              'type': 'success'
            })
          } else if (response.data.message === 'error') {
            this.$notify.error({
              'title': '错误',
              'message': '申请公共教室发生错误'
            })
          }
        }).catch(function () {
          console.log('error')
        })
      }
    },
    computed: {
      GetClubId () {
        return this.$cookie.get('ClubId')
      },
      GetClubToken () {
        return this.$cookie.get('ClubToken')
      }
    }
  }
</script>
<style>
</style>
