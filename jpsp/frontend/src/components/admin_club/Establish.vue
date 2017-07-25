<template>
  <div>
    <el-form ref="EstablishClubForm" :model="EstablishClubForm">
      <el-form-item label="社团名称" required>
        <el-input v-model="EstablishClubForm.ClubName"></el-input>
      </el-form-item>
      <el-form-item label="社长姓名" required>
        <el-input v-model="EstablishClubForm.ShezhangName"></el-input>
      </el-form-item>
      <el-form-item label="社长年级" required>
        <el-select v-model="EstablishClubForm.ShezhangGrade" value="">
          <el-option label="高一" value="1"></el-option>
          <el-option label="高二" value="2"></el-option>
          <el-option label="高三" value="3"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="社长班级" required>
        <el-select v-model="EstablishClubForm.ShezhangClassroom" value="">
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
      <el-form-item label="社长QQ号" required>
        <el-input v-model="EstablishClubForm.ShezhangQQ"></el-input>
      </el-form-item>
      <el-form-item label="是否进行招新" required>
        <el-radio-group v-model="EstablishClubForm.IfRecruit">
          <el-radio :label=true>招新</el-radio>
          <el-radio :label=false>不招新</el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item label="招新QQ群" required>
        <el-input v-if="EstablishClubForm.IfRecruit" v-model="EstablishClubForm.QQGroup"></el-input>
      </el-form-item>
      <el-form-item label="社团邮箱">
        <el-input v-model="EstablishClubForm.Email"></el-input>
      </el-form-item>
      <el-form-item label="社团介绍" required>
        <el-input type="textarea" v-model="EstablishClubForm.Introduction"></el-input>
      </el-form-item>
      <el-form-item label="社团类型" required>
        <el-checkbox-group v-model="EstablishClubForm.Label">
          <el-checkbox label="人文"></el-checkbox>
          <el-checkbox label="科技"></el-checkbox>
          <el-checkbox label="计算机"></el-checkbox>
          <el-checkbox label="摄影"></el-checkbox>
          <el-checkbox label="体育"></el-checkbox>
          <el-checkbox label="艺术"></el-checkbox>
          <el-checkbox label="学科类"></el-checkbox>
        </el-checkbox-group>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm('EstablishForm')">立即创建</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>
<script>
  import axios from 'axios'
  export default {
    data () {
      return {
        EstablishClubForm: {
          ClubName: '',
          ShezhangName: '',
          ShezhangQQ: '',
          ShezhangGrade: '',
          ShezhangClassroom: '',
          Label: [],
          Introduction: '',
          IfRecruit: true,
          QQGroup: '',
          Email: ''
        }
      }
    },
    methods: {
      submitForm () {
        axios({
          method: 'POST',
          url: 'api/club/establish',
          data: JSON.stringify({
            Clubname: this.EstablishClubForm.ClubName,
            Shezhang_Name: this.EstablishClubForm.ShezhangName,
            Shezhang_QQ: this.EstablishClubForm.ShezhangQQ,
            Shezhang_Grade: this.EstablishClubForm.ShezhangGrade,
            Shezhang_Classroom: this.EstablishClubForm.ShezhangClassroom,
            Introduction: this.EstablishClubForm.Introduction,
            IfRecruit: this.EstablishClubForm.IfRecruit,
            QQGroup: this.EstablishClubForm.QQGroup,
            Email: this.EstablishClubForm.Email
          })
        }).then(function (response) {
          if (response.data.message === 'success') {
            this.$notify({
              title: '成功',
              message: '成功创建社团',
              type: 'success'
            })
          }
          if (response.data.message === 'error') {
            this.$notify.error({
              title: '错误',
              message: '无法创建社团'
            })
          }
        }.bind(this)).catch(function () {
          this.$notify.error({
            title: '错误',
            message: '无法创建社团'
          })
        })
      }
    }
  }
</script>
<style>
</style>
