<!---component jfooter-->
<template>
<div class="container">
<el-row>
  <el-col :span='24' align="right"><a href="#">Back to top</a></el-col>
</el-row>
<el-row>
  <el-col :span='24' align="left">地址：浦东崮山路517号 、385号(北校区)</el-col>
</el-row>
<el-row>
  <el-col :span='24' align="left">电话 / 传真：021-58851542 / 021-38821698</el-col>
</el-row>
<el-row>
  <el-col :span='24' align="left">邮箱：jpzxxzyx2016@163.com</el-col>
</el-row>
<el-row>
  <el-col :span='24' align="left">地址：浦东崮山路517号 、385号(北校区)</el-col>
</el-row>
<el-row>
  <el-col :span='24' align="left">版权所有：Jeek</el-col>
</el-row>
<el-row>
  <el-col :span='24' align="left"><a href="#">Privacy</a><a href="#">Terms</a><a href="#">Contributors</a></el-col>
</el-row>
</div>
</template>
<script>
  export default {
    data () {
      return {
        msg: 'footer'
      }
    },
    methods: {
      handleSelect (key, keyPath) {
        console.log(key, keyPath)
      }
    }
  }
</script>
<style>
  @import url("//unpkg.com/element-ui@1.3.2/lib/theme-default/index.css");

  .container{
    background-color: #324057;
    color: #a4aebd;
    height: 100%;
    padding: 10px 40px 20px 100px;
  }

  .container a{
    display: inline-block;
    color: #768193;
    margin: 12px 18px 0 0;
    line-height: 1;
  }
</style>
