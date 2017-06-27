<template>
  <div>
    <el-form ref="PostForm" :model="PostForm" label-width="80px">
      <el-form-item label="姓名">
        <el-input v-model="PostForm.Name"></el-input>
      </el-form-item>
      <el-form-item prop="PostForm.Grade" label="年级" :required="true">
        <el-select v-model="PostForm.Grade" value="">
          <elm-option label="高一" value="1"></elm-option>
          <el-option label="高二" value="2"></el-option>
          <el-option label="高三" value="3"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item prop="PostForm.Class" label="班级" :required="true">
        <el-select v-model="PostForm.Class" value="">
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
        <el-input v-model="PostForm.QQ"></el-input>
      </el-form-item>
      <el-form-item label="Email" prop="Email">
        <el-input v-model="PostForm.Email"></el-input>
      </el-form-item>
      <el-form-item label="Phone" prop="Phone">
        <el-input v-model="PostForm.Phone"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">立即创建</el-button>
        <el-button>取消</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>
<script>
  import axios from 'axios'
  export default {
    data () {
      return {
        PostForm: {
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
    mounted: function () {
      axios({
        method: 'GET',
        url: 'http://127.0.0.1:8000/api/cd/post/list'
      })
        .then(function (response) {
          if (response.data.message === 'success') {
            this.PostListTable = JSON.parse(response.data.data)
            console.log(this.PostListTable)
            console.log('success')
          } else {
            console.log('error')
          }
        }.bind(this))
    }
  }
</script>
<style scoped>
  @import url("//unpkg.com/element-ui@1.3.2/lib/theme-default/index.css");
</style>
