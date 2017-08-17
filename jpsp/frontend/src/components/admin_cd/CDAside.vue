<template>
  <aside class="menu">
    <p class="menu-label">
      总览
    </p>
    <ul class="menu-list">
      <li>
        <router-link to="/dashboard">仪表盘</router-link>
      </li>
    </ul>
    <p class="menu-label">
      社团活动记录
    </p>
    <ul class="menu-list">
      <li>
        <router-link to="/post/list">列表</router-link>
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
        <router-link to="/activity/list">列表</router-link>
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
  </aside>
</template>
<script>
</script>
<style>
</style>
