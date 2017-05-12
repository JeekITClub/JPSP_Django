<template>
  <el-row>
    <el-col :span="24">
      <div class="grid-content bg-purple-dark">
        <el-menu theme="dark" :default-active="activeIndex" class="el-menu-demo" mode="horizontal"
                 @select="handleSelect">
          <el-menu-item index="1" disabled="" route="">处理中心</el-menu-item>
          <el-submenu index="2">
            <template slot="title">我的工作台</template>
            <el-menu-item index="2-1" disabled="" route="">选项1</el-menu-item>
            <el-menu-item index="2-2" disabled="" route="">选项2</el-menu-item>
            <el-menu-item index="2-3" disabled="" route="">选项3</el-menu-item>
          </el-submenu>
          <el-menu-item index="3" disabled="" route=""><a href="https://www.ele.me" target="_blank">订单管理</a>
          </el-menu-item>
        </el-menu>
      </div>
    </el-col>
  </el-row>
</template>
<script>

</script>
<style>
  .el-row {
    margin-bottom: 20px;

  &
  :last-child {
    margin-bottom: 0;
  }

  }
  .bg-purple-dark {
    background: #99a9bf;
  }

  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }

</style>
