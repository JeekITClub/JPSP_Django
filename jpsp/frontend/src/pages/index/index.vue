<template>
<div>
<el-row class="content-container welcome">
<el-col :span="14" class="login-text">
  <p>社团</p>
  <p>从未如此简单</p>
</el-col>
<el-col :span="10" class="login-form">
<div class="form">
<h2>进入社团的奇妙世界</h2>
<br>
<el-form label-position="top" ref="form" :model="form" label-width="80px">
  <el-form-item label="用户名">
    <el-input v-model="form.username"></el-input>
  </el-form-item>
  <el-form-item label="密码">
    <el-input v-model="form.password"></el-input>
  </el-form-item>
  <el-form-item label="">
    <el-radio v-model="form.remember" :label="true">记住我</el-radio>
  </el-form-item>
  <el-form-item>
    <el-button type="primary" @click="onSubmit" class="login-button">登录</el-button>
  </el-form-item>
</el-form>
</div>
</el-col>
</el-row>

<div class="main-content">
<div class="content-container">
<el-row>
<el-col :span="12" class="intro">
Write Better Code.
</el-col>
<el-col :span="12" class="image" align="right">
Image</el-col>
</el-row>
</div>

<div class="content-container">
<el-row>
<el-col :span="12" class="image" align="right">
Image
</el-col>
<el-col :span="12" class="intro">
Write Better Code.
</el-col>
</el-row>
</div>

<div class="content-container">
<el-row>
<el-col :span="12" class="intro">
Write Better Code.
</el-col>
<el-col :span="12" class="image" align="right">
Image
</el-col>
</el-row>
</div>

</div>
</div>
</template>
<script>
  export default {
    data () {
      return {
        form: {
          username: '',
          password: '',
          remember: false
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
<style>
  @import url("//unpkg.com/element-ui@1.3.2/lib/theme-default/index.css");

  body{
    margin: 0px;
  }

  .content-container{
    height: 100vh;
  }

  .welcome{
    padding-top: 40px;
    padding-bottom: 60px;
    background-color: #20a0ff;
    opacity: 0.75;
  }

  .login-text{
    padding-top: 80px;
    padding-left: 180px;
    font-size: 4em;
    height: 100%;
  }

  .login-form{
    padding-top: 10px;
    padding-bottom: 20px;
    padding-right: 150px;
    height: 100%;
  }

  .form{
    height: 100%;
    background-color: #ffffff;
    border-radius: 3px;
    padding: 36px;
    border: 1px solid #d1d5da;
    box-sizing: border-box;
  }

  .login-button{
    width: 100%;
  }

  .main-content{
  }

  .content{
    padding: 20px;
  }

  .el-carousel__item h3 {
    color: #475669;
    font-size: 18px;
    opacity: 0.75;
    line-height: 300px;
    margin: 0;
  }
  
  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }
  
  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }

  .intro{
    padding-left: 40vh;
    line-height: 100vh;
    font-size: 3em;
  }

  .image{
    padding-right: 40vh;
    line-height: 100vh;
    font-size: 3em;
  }
</style>
