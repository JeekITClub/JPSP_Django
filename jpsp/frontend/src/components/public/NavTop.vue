<!---component nav-top-->
<template>
<div>
<el-row>
<el-col :span="24">
  <el-menu class="el-menu-demo" mode="horizontal" unique-opened="true" @select="handleSelect">
  <el-menu-item index="1" style="font-size: 1.5em;">建平学生社团平台</el-menu-item>
  <el-menu-item index="2">社团动态</el-menu-item>
  <el-menu-item index="3">社团介绍</el-menu-item>
  <el-menu-item index="4">活动报名</el-menu-item>
</el-menu>
</el-col>
</el-row>
</div>
</template>
<script>
  export default {
    data () {
      return {
        activeIndex: '1',
        activeIndex2: '1'
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

  .el-menu{
    background-color: rgb(32, 160, 255);
  }
</style>
