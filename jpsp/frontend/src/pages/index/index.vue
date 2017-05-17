<template>
<div>
<el-row class="content-container welcome">
<el-col :span="14" class="login-text">
  <p>社团</p>
  <p>从未如此简单</p>
</el-col>
<el-col :span="10" class="login-form">
<div class="form">
<el-row><h2>进入社团的奇妙世界</h2 ></el-row>
<el-row><p>用户名</p></el-row>
  <el-row>
  <el-input v-model="username" placeholder="用户名"></el-input>
  </el-row>
  <el-row><p>密码</p></el-row>
  <el-row>
  <el-input v-model="password" placeholder="密码"></el-input>
  </el-row>
  <br>
  <el-row><el-radio class="radio" v-model="remember" label="remember">记住我</el-radio></el-row>
  <br>
  <el-row><el-button type="primary" size="large"  class="login-button">登录</el-button></el-row>
  <p>{{ remember }}</p>
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
        username: '',
        password: '',
        remember: false
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
