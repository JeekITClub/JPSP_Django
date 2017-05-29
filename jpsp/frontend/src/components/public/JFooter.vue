<!---component jfooter-->
<template>
    <footer class="footer">
      <div class="container">
        <el-row>
          <el-col :span='6' align="left" offset="6">地址：浦东崮山路517号 、385号(北校区)</el-col>
          <el-col :span='6' align="left">电话 / 传真：021-58851542 / 021-38821698</el-col>
        </el-row>
        <el-row>
          <el-col :span='6' align="left" offset="6">邮箱：jpzxxzyx2016@163.com</el-col>
          <el-col :span='6' align="left">版权所有：Jeek</el-col>
        </el-row>
      </div>
    </footer>
</template>
<script>
  export default {
    data () {
      return {}
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

  .footer {
    position: relative;
    bottom: 0;
    width: 100%;
    height: 6%;
    background-color: #f5f5f5;
  }
  .footer .container {
    padding-top: 10px;
  }
</style>
