<!---component dashboard aside-->
<template>
      <el-menu @open="handleOpen" @close="handleClose">
        <el-menu-item index="7" disabled="" route=""><i class="el-icon-menu"></i>仪表盘</el-menu-item>
        <el-submenu index="2">
          <template slot="title">
            <i class="el-icon-document"></i>社团动态
          </template>
          <el-menu-item-group>
            <el-menu-item index="2-1" route="" disabled="">概览</el-menu-item>
            <el-menu-item index="2-2" route="" disabled="">A</el-menu-item>
            <el-menu-item index="2-3" route="" disabled="">B</el-menu-item>
            <el-menu-item index="2-4" route="" disabled="">C</el-menu-item>
          </el-menu-item-group>
        </el-submenu>
        <el-submenu index="3">
          <template slot="title">
            <i class="el-icon-document"></i>XXXX
          </template>
          <el-menu-item-group>
            <el-menu-item index="3-1" route="" disabled="">概览</el-menu-item>
            <el-menu-item index="3-2" route="" disabled="">A</el-menu-item>
            <el-menu-item index="3-3" route="" disabled="">B</el-menu-item>
            <el-menu-item index="3-4" route="" disabled="">C</el-menu-item>
          </el-menu-item-group>
        </el-submenu>
        <el-submenu index="4">
          <template slot="title">
            <i class="el-icon-document"></i>XXXX
          </template>
          <el-menu-item-group>
            <el-menu-item index="4-1" route="" disabled="">概览</el-menu-item>
            <el-menu-item index="4-2" route="" disabled="">A</el-menu-item>
            <el-menu-item index="4-3" route="" disabled="">B</el-menu-item>
            <el-menu-item index="4-4" route="" disabled="">C</el-menu-item>
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
      }
    }
</script>
<style>
  @import url("//unpkg.com/element-ui@1.3.2/lib/theme-default/index.css");
</style>
