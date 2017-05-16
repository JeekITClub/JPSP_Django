<template>
<el-form ref="form" :model="PostForm" label-width="100%">
  <el-form-item label="社团名称">
    <el-input v-model="PostForm.ClubName"></el-input>
  </el-form-item>
  <el-form-item label="社长">
    <el-input v-model="PostForm.Shezhang.Name"></el-input>
  </el-form-item>
  <el-form-item label="社长QQ">
    <el-input v-model="PostForm.Shezhang.QQ"></el-input>
  </el-form-item>
  <el-form-item prop="PostForm.Shezhang.Grade" label="社长年级">
    <el-select v-model="PostForm.Shezhang.Grade" >
        <el-option label="高一" value="1"></el-option>
        <el-option label="高二" value="2"></el-option>
        <el-option label="高三" value="3"></el-option>
    </el-select>
  </el-form-item>
  <el-form-item prop="PostForm.Shezhang.Class" label="社长班级">
        <el-select v-model="PostForm.Shezhang.Class" >
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
  <el-form-item label="是否进行招新">
    <el-radio-group v-model="PostForm.IfRecruit">
      <el-radio :label=true>招新</el-radio>
      <el-radio :label=false>不招新</el-radio>
    </el-radio-group>
  </el-form-item>
  <el-form-item label="招新QQ群">
    <el-input v-if="PostForm.IfRecruit" v-model="PostForm.QQGroup"></el-input>
  </el-form-item>
  <el-form-item label="社长邮箱">
    <el-input v-model="PostForm.Email"></el-input>
  </el-form-item>
  <el-form-item label="社团介绍">
    <el-input type="textarea" v-model="PostForm.introduction"></el-input>
  </el-form-item>
  <el-form-item label="社团类型">
    <el-checkbox-group v-model="PostForm.Type">
      <el-checkbox label="人文"></el-checkbox>
      <el-checkbox label="科技"></el-checkbox>
      <el-checkbox label="计算机"></el-checkbox>
      <el-checkbox label="摄影"></el-checkbox>
      <el-checkbox label="体育"></el-checkbox>
      <el-checkbox label="艺术"></el-checkbox>
      <el-checkbox label="学科类"></el-checkbox>
    </el-checkbox-group>
  </el-form-item>
  <el-form-item
    label="社团成就"
    v-for="(achievement, index) in PostForm.achievements"
    :label="'成就' + index"
    :key="achievements.key"
    :prop="'achievement.' + index + '.value'"
    :rules="{
      required: true, message: '不能为空', trigger: 'blur'
    }"
  >
    <el-input v-model="achievements.value"></el-input><el-button @click.prevent="removeAchievement(achievement)">删除</el-button>
  </el-form-item>
  <el-form-item>
    <el-button @click="addAchievement">新增成就</el-button>
  </el-form-item>
  <el-form-item>
    <el-button type="primary" @click="onSubmit">提交修改</el-button>
    <el-button>取消</el-button>
  </el-form-item>
</el-form>
</template>
<script>
  export default {
    data () {
      return {
        PostForm: {
          ClubName: '',
          Date1: '',
          Date2: '',
          Date3: '',
          Type: [],
          introduction: '',
          IfRecruit: true,
          achievements: [
            {
              value: ''
            }
          ],
          Email: '',
          Shezhang: [
            {
              Name: '',
              QQ: '',
              Grade: '',
              Class: ''
            }
          ]
        }
      }
    },
    methods: {
      onSubmit () {
        console.log('submit!');
      },
      submitForm (formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            alert('submit!')
          } else {
            console.log('error submit!!')
            return false
          }
        })
      },
      removeAchievement (item) {
        var index = this.PostForm.achievements.indexOf(item)
        if (index !== -1) {
          this.PostForm.achievements.splice(index, 1)
        }
      },
      addAchievement () {
        this.PostForm.ahievements.push({
          value: '',
          key: Date.now()
        })
      }
    }
  }
</script>
<style>
  @import url("//unpkg.com/element-ui@1.3.2/lib/theme-default/index.css");
</style>
