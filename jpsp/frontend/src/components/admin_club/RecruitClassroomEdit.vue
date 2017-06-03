<template>
  <div v-if="Authenticate===true">
    <el-form ref="PostForm" :model="PostForm">
      <el-form-item label="社团名称" required prop="ClubName">
        <el-input v-bind="PostForm.ClubName">
        </el-input>
      </el-form-item>
      <el-form-item label="公共教室需要时间" required>
        <el-col :span="4">
          <el-form-item prop="Date1" required>
            <el-date-picker type="date" placeholder="选择日期" v-model="PostForm.Date1"
                            style="width: 100%;"></el-date-picker>
          </el-form-item>
        </el-col>
        <el-col class="line" :span="4"></el-col>
        <el-col :span="4">
          <el-form-item prop="Date2" required>
            <el-time-picker type="fixed-time" placeholder="选择开始时间" v-model="PostForm.Date2"
                            style="width: 100%;"></el-time-picker>
          </el-form-item>
        </el-col>
        <el-col class="line" :span="4"></el-col>
        <el-col :span="4">
          <el-form-item prop="Date3" required>
            <el-time-picker type="fixed-time" placeholder="选择结束时间" v-model="PostForm.Date3"
                            style="width: 100%;"></el-time-picker>
          </el-form-item>
        </el-col>
      </el-form-item>
      <el-form-item>
        <el-button type="primary"></el-button><!-- TODO: button-->
      </el-form-item>
    </el-form>
  </div>
</template>
<script>
  export default {
    name: 'RecruitClassroomApply',
    data () {
      return {
        PostForm: {
          ClubName: '',
          Date1: '',
          Date2: '',
          Date3: ''
        }
      }
    },
    methods: {},
    computed: {
      Authenticate () {
        return this.$store.state.Authenticated
      }
    }
  }
</script>
<style>
</style>
