<!---component dashboard aside-->
<template>
  <el-menu @open="handleOpen" @close="handleClose">
    <el-menu-item index="7" disabled="" route=""><i class="el-icon-menu"></i>仪表盘</el-menu-item>
    <el-submenu index="2">
      <template slot="title">
        <i class="el-icon-document"></i>社团动态
      </template>
      <el-menu-item-group>
        <el-menu-item index="2-1" route="" disabled="">
          <router-link to="/post/history">历史</router-link>
        </el-menu-item>
        <el-menu-item index="2-2" route="" disabled="">添加</el-menu-item>
      </el-menu-item-group>
    </el-submenu>
    <el-submenu index="3">
      <template slot="title">
        <i class="el-icon-document"></i>成员
      </template>
      <el-menu-item-group>
        <el-menu-item index="3-1" route="" disabled="">成员管理</el-menu-item>
      </el-menu-item-group>
    </el-submenu>
    <el-submenu index="4">
      <template slot="title">
        <i class="el-icon-document"></i>招新
      </template>
      <el-menu-item-group>
        <el-menu-item index="4-1" route="" disabled="">概览</el-menu-item>
        <el-menu-item index="4-2" route="/recruit/classroom" disabled="">公共教室申请</el-menu-item>
        <el-menu-item index="4-3" route="/recruit/" disabled="">新社员审核</el-menu-item>
      </el-menu-item-group>
    </el-submenu>
    <el-submenu index="5">
      <template slot="title">
        <i class="el-icon-document"></i>XXXX
      </template>
      <el-menu-item-group>
        <el-menu-item index="5-1" route="" disabled="">概览</el-menu-item>
        <el-menu-item index="5-2" route="" disabled="">A</el-menu-item>
        <el-menu-item index="5-3" route="" disabled="">B</el-menu-item>
        <el-menu-item index="5-4" route="" disabled="">C</el-menu-item>
      </el-menu-item-group>
    </el-submenu>
    <el-submenu index="6">
      <template slot="title">
        <i class="el-icon-document"></i>XXX
      </template>
      <el-menu-item-group>
        <el-menu-item index="6-1" route="" disabled="">概览</el-menu-item>
        <el-menu-item index="6-2" route="" disabled="">A</el-menu-item>
        <el-menu-item index="6-3" route="" disabled="">B</el-menu-item>
        <el-menu-item index="6-4" route="" disabled="">C</el-menu-item>
      </el-menu-item-group>
    </el-submenu>
    <el-menu-item index="7" disabled="" route=""><i class="el-icon-setting"></i>导航三</el-menu-item>
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
