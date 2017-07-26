<template>
  <el-menu>
    <el-menu-item index="1" disabled="">仪表盘</el-menu-item>
    <el-submenu index="2">
      <template slot="title">
        社团活动记录
      </template>
      <el-menu-item-group>
        <el-menu-item index="2-1" disabled=""><router-link to="/post/list">列表</router-link> </el-menu-item>
        <el-menu-item index="2-2" disabled=""><router-link to="/post/submit">添加</router-link></el-menu-item>
        <el-menu-item index="2-3" disabled="">数据分析（开发中）</el-menu-item>
      </el-menu-item-group>
    </el-submenu>
    <el-submenu index="3">
      <template slot="title">
        成员/招新
      </template>
      <el-menu-item-group>
        <el-menu-item index="3-1" disabled=""><router-link to="/member">成员管理</router-link></el-menu-item>
        <el-menu-item index="3-2" disabled=""><router-link to="/recruit/classroom/apply">公共教室申请</router-link></el-menu-item>
        <el-menu-item index="3-3" disabled=""><router-link to="/recruit/classroom/list">公共教室列表</router-link></el-menu-item>
      </el-menu-item-group>
    </el-submenu>
    <el-submenu index="4">
      <template slot="title">
        活动
      </template>
      <el-menu-item-group>
        <el-menu-item index="4-1" disabled="">概览</el-menu-item>
        <el-menu-item index="4-2" disabled="">申请</el-menu-item>
      </el-menu-item-group>
    </el-submenu>
  </el-menu>
</template>
<script>
</script>
<style>
</style>
