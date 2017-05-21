<template>
  <div>
    <el-menu theme="dark" :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
      <el-menu-item index="1" disabled="" route="">建平中学学生社团系统</el-menu-item>
      <el-badge v-bind:value="value" class="item">
        <el-button size="small">评论</el-button>
      </el-badge>
    </el-menu>
    <div class="line"></div>
  </div>
</template>
<script>
  export default {
    data () {
      return {
        value: '2'
      }
    },
    methods: {
      handleSelect (key, keyPath) {
        console.log(key, keyPath)
      }
    }
  }
</script>
