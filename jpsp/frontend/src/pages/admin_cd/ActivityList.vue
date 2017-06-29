<template>
  <div>
    <el-row class="tac">
      <el-col :span="4">
        <cd_aside></cd_aside>
      </el-col>
      <el-col :span="20" offset="4">
        <cd_activity_list></cd_activity_list>
      </el-col>
    </el-row>
  </div>
</template>
<script>
  import CDAside from '../../components/admin_cd/CDAside.vue'
  import ActivityList from '../../components/public/ActivityList.vue'
  export default {
    components: {
      'cd_aside': CDAside,
      'cd_activity_list': ActivityList
    },
    data () {
      return {}
    }
  }
</script>
<style>
</style>
