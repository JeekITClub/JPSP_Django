<template>
  <el-form ref="form" :model="ActivityApplyForm">
    <el-form-item label="活动名称">
      <el-input v-model="ActivityApplyForm.ActivityName" placeholder="请输入活动名称"></el-input>
    </el-form-item>
    <el-form-item label="活动地点">
      <el-input v-model="ActivityApplyForm.Region" placeholder="请输入活动地点">
      </el-input>
    </el-form-item>
    <el-form-item label="活动时间">
      <el-row>
        <el-col :span="6">
          <el-date-picker type="date" placeholder="选择日期" v-model="ActivityApplyForm.Date1"></el-date-picker>
        </el-col>
        <el-col :span="6" :offset="1">
          <el-time-picker type="" placeholder="选择开始时间" v-model="ActivityApplyForm.Date2"></el-time-picker>
        </el-col>
        <el-col :span="6" :offset="1">
          <el-time-picker type="" placeholoder="选择结束时间" v-model="ActivityApplyForm.Date3"></el-time-picker>
        </el-col>
      </el-row>
    </el-form-item>
    <!--<el-form-item label="活动类型">-->
    <!--<el-select placeholder="请选择活动类型">-->
    <!--<el-option :key=""></el-option>-->
    <!--&lt;!&ndash;TODO: define the type&ndash;&gt;-->
    <!--</el-select>-->
    <!--</el-form-item>-->
    <el-form-item label="活动内容">
      <el-input type="textarea" v-model="ActivityApplyForm.Content" placeholder="请输入活动内容"></el-input>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="submitForm">立即申请</el-button>
      <el-button>取消</el-button>
    </el-form-item>
  </el-form>
</template>
<script>
  // 活动申请组件
  import axios from 'axios'
  export default {
    data () {
      return {
        ActivityApplyForm: {
          ClubName: this.GetClubName,
          ActivityName: '',
          Region: '',
          Date1: '',
          Date2: '',
          Date3: '',
          Type: '',
          Content: ''
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
            ClubName: this.GetClubName,
            ActivityName: this.ActivityApplyForm.ActivityName,
            Region: this.ActivityApplyForm.Region,
            Date1: this.ActivityApplyForm.Date1,
            Date2: this.ActivityApplyForm.Date2,
            Date3: this.ActivityApplyForm.Date3,
            Content: this.ActivityApplyForm.Content,
            Type: this.Type,
            Token: this.GetToken
          }),
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
          }
        }).then(function (response) {
          if (response.data.message === 'success') {
            console.log('success')
          }
          if (response.data.message === 'error') {
            console.log('error')
          }
        }).catch(function () {
          alert('error: ActivityApply')
        })
      },
      resetForm (formName) {
        this.$refs[formName].resetFields()
      }
    },
    computed: {
      GetClubName () {
        return this.$cookie.get('ClubName')
      },
      GetClubId () {
        return this.$cookie.get('ClubName')
      },
      GetToken () {
        return this.$cookie.get('ClubToken')
      }
    }
  }
</script>
<style>
</style>
