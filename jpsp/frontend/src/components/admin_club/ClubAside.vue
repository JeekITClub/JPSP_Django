<!---component dashboard aside-->
<template>
  <el-menu @open="handleOpen" @close="handleClose">
    <el-menu-item index="1" disabled="" route="/">>仪表盘</el-menu-item>
    <el-submenu index="2">
      <template slot="title">
        社团活动记录
      </template>
      <el-menu-item-group>
        <el-menu-item index="2-1" route="" disabled="">
          <router-link to="/post/history">历史</router-link>
        </el-menu-item>
        <el-menu-item index="2-2" route="" disabled="">添加</el-menu-item>
        <el-menu-item index="2-3" route="" disabled="">数据分析</el-menu-item>
      </el-menu-item-group>
    </el-submenu>
    <el-submenu index="3">
      <template slot="title">
        成员/招新
      </template>
      <el-menu-item-group>
        <el-menu-item index="3-1" route="" disabled="">成员管理</el-menu-item>
        <el-menu-item index="3-2" route="/recruit/" disabled="">新社员审核</el-menu-item>
        <el-menu-item index="3-3" route="/recruit/classroom" disabled="">公共教室申请</el-menu-item>
      </el-menu-item-group>
    </el-submenu>
    <el-submenu index="4">
      <template slot="title">
        活动
      </template>
      <el-menu-item-group>
        <el-menu-item index="4-1" route="" disabled="">概览</el-menu-item>
        <el-menu-item index="4-2" route="" disabled="">申请</el-menu-item>
      </el-menu-item-group>
    </el-submenu>
  </el-menu>
</template>
<script>
  export default {
    methods: {
      handleOpen (key, keyPath) {
        console.log(key, keyPath)
      },
      handleClose (key, keyPath) {
        console.log(key, keyPath)
      }
    },
    computed: {
      Authenticate () {
        return this.$store.state.Authenticated
      }
    }
  }
</script>
<style>
</style>
