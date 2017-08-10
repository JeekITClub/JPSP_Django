<template>
  <div>
    <el-upload class="upload-demo" :action="this.GetUploadUrl" :on-remove="handleRemove" :file-list="fileList" data="">
      <el-button size="small" type="primary">点击上传</el-button>
      <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div>
    </el-upload>
  </div>
</template>
<script>
  // import axios from 'axios'
  export default {
    data () {
      return {
        fileList: []
      }
    },
    computed: {
      /**
       * @return {string}
       */
      GetApi () {
        return this.$store.state.Api
      },
      /**
       * @return {string}
       */
      GetUploadUrl () {
        return this.GetAPI + '/file/upload'
      }
    }
  }
</script>
<style>
</style>
