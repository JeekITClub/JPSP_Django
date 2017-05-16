<template>
<div>
<el-row class="carousel">
<el-col :span="24">
  <el-carousel :interval="5000" arrow="always" height="90vh">
    <el-carousel-item v-for="item in 4" :key="item">
      <h3>{{ item }}</h3>
    </el-carousel-item>
  </el-carousel>
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
    data: {
      items: [
      ]
    },
    methods: {
      handleOpen (key, keyPath) {
        console.log(key, keyPath)
      },
      handleClose (key, keyPath) {
        console.log(key, keyPath)
      }
    }
  }
</script>
<style>
  @import url("//unpkg.com/element-ui@1.3.2/lib/theme-default/index.css");

  .content-container{
    height: 100vh;
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
