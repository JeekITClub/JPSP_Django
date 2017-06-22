<template>
  <div>
    <el-row class="tac">
      <el-col :span="4">
        <cd_aside></cd_aside>
      </el-col>
      <el-col :span="20">
        <cd_post_list></cd_post_list>
      </el-col>
    </el-row>
  </div>
</template>
<script>
  import PostList from '../../components/admin_cd/PostList.vue'
  import CDAside from '../../components/admin_cd/CDAside.vue'
  export default {
    components: {
      'cd_aside': CDAside,
      'cd_post_list': PostList
    },
    data () {
      return {}
    }
  }
</script>
<style>
</style>
