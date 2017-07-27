<template>
  <el-row :gutter="20">
    <el-col :span=4>
      <setting_aside></setting_aside>
    </el-col>
    <el-col :span=20>
      <el-form ref="ProfileForm" :model="ProfileForm">
        <el-form-item prop="Name" label="姓名" :required="true">
          <el-input v-model="ProfileForm.Name"></el-input>
        </el-form-item>
        <el-form-item prop="Grade" label="年级" :required="true">
          <el-select v-model="ProfileForm.Grade" value="">
            <el-option label="高一" value="1"></el-option>
            <el-option label="高二" value="2"></el-option>
            <el-option label="高三" value="3"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item prop="Class" label="班级" :required="true">
          <el-select v-model="ProfileForm.Class" value="">
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
        <el-form-item label="QQ" prop="QQ">
          <el-input v-model="ProfileForm.QQ"></el-input>
        </el-form-item>
        <el-form-item label="电子邮箱" prop="Email">
          <el-input v-model="ProfileForm.Email"></el-input>
        </el-form-item>
        <el-form-item label="手机号码" prop="Phone">
          <el-input v-model="ProfileForm.Phone"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmit()">更改</el-button>
          <el-button>取消</el-button>
        </el-form-item>
      </el-form>
    </el-col>
  </el-row>
</template>
<script>
  import SettingAside from '../../components/index/SettingAside.vue'
  import axios from 'axios'
  export default {
    components: {
      'setting_aside': SettingAside
    },
    data () {
      return {
        ProfileForm: {
          Name: '',
          Grade: '',
          Class: '',
          QQ: '',
          Email: '',
          Phone: ''
        }
      }
    },
    computed: {
      Authenticate () {
        return this.$store.state.Authenticated
      },
      GetToken () {
        return this.$store.state.Token
      },
      GetUserName () {
        return this.$store.state.UserName
      }
    },
    methods: {
      onSubmit () {
        axios({
          method: 'POST',
          url: '',
          data: JSON.stringify({
            'Name': this.ProfileForm.Name,
            'Grade': this.ProfileForm.Grade,
            'Class': this.ProfileForm.Class,
            'QQ': this.ProfileForm.QQ,
            'Email': this.ProfileForm.Email,
            'Phone': this.ProfileForm.Phone
          })
        })
      }
    },
    mounted: function () {
      axios({
        method: 'GET',
        url: 'http://127.0.0.1:8000/api/userprofile/get'
      })
        .then(function (response) {
          if (response.data.message === 'success') {
            this.ProfileForm = JSON.parse(response.data.data)
          } else {
            this.$notify.error({
              title: '错误',
              message: '无法获得数据'
            })
          }
        }.bind(this))
    }
  }
</script>
<style scoped>
</style>
