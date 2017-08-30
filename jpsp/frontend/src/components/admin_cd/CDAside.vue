<template>
  <aside class="menu">
    <p class="menu-label">
      总览
    </p>
    <ul class="menu-list">
      <li>
        <router-link to="/">仪表盘</router-link>
      </li>
    </ul>
    <p class="menu-label">
      社团
    </p>
    <ul class="menu-list">
      <li>
        <router-link to="/club">所有社团</router-link>
      </li>
      <li>
        <router-link to="/post">动态</router-link>
      </li>
    </ul>
    <p class="menu-label">
      招新
    </p>
    <ul class="menu-list">
      <li>
        <router-link to="/recruit/classroom/list">公共教室列表</router-link>
      </li>
    </ul>
    <p class="menu-label">
      活动
    </p>
    <ul class="menu-list">
      <li>
        <router-link to="/activity">列表</router-link>
      </li>
    </ul>
    <p class="menu-label">
      文件
    </p>
    <ul class="menu-list">
      <li>
        <router-link to="/file/upload">上传</router-link>
      </li>
      <li>
        <router-link to="/file/download">下载</router-link>
      </li>
    </ul>
    <p class="menu-label">
      用户
    </p>
    <ul class="menu-list">
      <li>
        <router-link to="/user">批量创建用户</router-link>
        <router-link to="/user/one">创建单一用户</router-link>
      </li>
    </ul>
  </aside>
</template>
<script>
</script>
<style>
</style>
