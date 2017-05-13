<template>
  <el-form ref="form" :model="form">
    <el-form-item label="用户名">
      <el-input v-model="form.username" placeholder="用户名"></el-input>
    </el-form-item>
    <el-form-item label="密码">
      <el-input v-model="form.password" placeholder="密码">
      </el-input>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="onSubmit">登陆</el-button>
    </el-form-item>
  </el-form>
</template>
<script>
  export default {
    data () {
      return {
        form: {
          name: '',
          password: ''
        }
      }
    },
    methods: {
      onSubmit () {
        console.log('submit!')
      }
    }
  }
</script>
<style>
  @import url("//unpkg.com/element-ui@1.3.2/lib/theme-default/index.css");
</style>
