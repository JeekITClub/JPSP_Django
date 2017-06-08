<template>
  <div>
    <el-form ref="form" :model="form">
      <el-form-item label="丢失物品名称" :required=true>
        <el-input v-model="form.name"></el-input>
      </el-form-item>
      <el-form-item label="丢失区域">
        <el-select v-model="form.region" placeholder="请选择丢失区域" value="">
          <el-option label="挹芬楼" value="yifen"></el-option>
          <el-option label="远翔楼" value="yuanxiang"></el-option>
          <el-option label="实验楼" value="shiyan"></el-option>
          <el-option label="行政楼" value="xingzheng"></el-option>
          <el-option label="济美楼" value="jimei"></el-option>
          <el-option label="体育馆" value="tiyu"></el-option>
          <el-option label="篮球场" value="lanqiu"></el-option>
          <el-option label="足球场" value="zuqiu"></el-option>
          <el-option label="金苹果大道" value="jinpingguodadao"></el-option>
          <el-option label="食堂" value="shitang"></el-option>
          <el-option label="宿舍" value="sushe"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="丢失时间">
        <el-col :span="11">
          <el-date-picker type="date" placeholder="选择日期" v-model="form.date1" style="width: 100%;"></el-date-picker>
        </el-col>
        <el-col class="line" :span="2">-</el-col>
        <el-col :span="11">
          <el-time-picker type="fixed-time" placeholder="选择时间" v-model="form.date2"
                          style="width: 100%;"></el-time-picker>
        </el-col>
      </el-form-item>
      <el-form-item label="重要物品">
        <el-switch :on-text="" :off-text="" v-model="form.importance"></el-switch>
      </el-form-item>
      <el-form-item label="物品描述">
        <el-input type="textarea" v-model="form.desc"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">立即创建</el-button>
        <el-button>取消</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>
<script>
  export default {
    data () {
      return {
        form: {
          name: '',
          region: '',
          date1: '',
          date2: '',
          importance: false,
          desc: ''
        }
      }
    },
    methods: {
      onSubmit () {
        console.log('submit!')
      }
    }
  }
</script>

