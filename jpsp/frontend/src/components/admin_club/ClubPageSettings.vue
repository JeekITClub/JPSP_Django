<template>
  <el-form ref="SettingsForm" :model="SettingsForm" v-if="Authenticate===true">
    <el-form-item></el-form-item>
  </el-form>
</template>
<script>
  //  可拖拽式社团个性主页
  export default {
    data () {
      return {
        SettingsForm: {}
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
