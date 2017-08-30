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
        <router-link to="/Club">所有社团</router-link>
      </li>
      <li>
        <router-link to="/Post">动态</router-link>
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
        <router-link to="/Activity">列表</router-link>
      </li>
    </ul>
    <p class="menu-label">
      文件
    </p>
    <ul class="menu-list">
      <li>
        <router-link to="/File/Upload">上传</router-link>
      </li>
      <li>
        <router-link to="/File/Download">下载</router-link>
      </li>
    </ul>
    <p class="menu-label">
      用户
    </p>
    <ul class="menu-list">
      <li>
        <router-link to="/User">批量创建用户</router-link>
        <router-link to="/User/One">创建单一用户</router-link>
      </li>
    </ul>
  </aside>
</template>
<script>
</script>
<style>
</style>
