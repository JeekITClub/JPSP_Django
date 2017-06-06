<template>
  <el-form ref="form" :model="PostForm" label-width="80px" v-if="Authenticate===true">
    <el-form-item label="社团名称">
      <el-input v-model="PostForm.ClubName"></el-input>
    </el-form-item>
    <el-form-item label="活动名称">
      <el-input v-model="PostForm.ActivityName" placeholder="请输入活动名称"></el-input>
    </el-form-item>
    <el-form-item label="活动地点">
      <el-input v-model="PostForm.region" placeholder="请输入活动地点">
      </el-input>
    </el-form-item>
    <el-form-item label="活动时间">
      <el-col :span="11">
        <el-date-picker type="date" placeholder="选择日期" v-model="PostForm.Date1" style="width: 100%;"></el-date-picker>
      </el-col>
      <el-col class="line" :span="2">-</el-col>
      <el-col :span="11">
        <el-time-picker type="fixed-time" placeholder="选择开始时间" v-model="PostForm.Date2"
                        style="width: 100%;"></el-time-picker>
      </el-col>
      <el-col :span="11">
        <el-time-picker type="fixed-time" placeholoder="选择结束时间" v-model="PostForm.Date3"
                        style="width: 100%;"></el-time-picker>
      </el-col>
    </el-form-item>
    <el-form-item label="活动内容">
      <el-input type="textarea" v-model="PostForm.Content"></el-input>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="onSubmit">立即申请</el-button>
      <el-button>取消</el-button>
    </el-form-item>
    <el-form-item label="活动类型">
    </el-form-item>

  </el-form>
</template>
<script>
  // 活动申请组件
  import axios from 'axios'
  export default {
    data () {
      return {
        PostForm: {
          ClubName: '',
          ActivityName: '',
          Region: '',
          Date1: '',
          Date2: '',
          Date3: '',
          Type: []
        }
      }
    },
    methods: {
      onSubmit () {
        console.log('submit!')
      },
      submitForm (formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            alert('submit!')
            axios.post('api/ClubActivityApplySubmit', {})
          } else {
            console.log('error submit!!')
            return false
          }
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
