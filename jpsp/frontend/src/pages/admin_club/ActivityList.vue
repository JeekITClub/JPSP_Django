<template>
  <div>
    <el-row class="tac">
      <el-col :span="4">
        <club_aside></club_aside>
      </el-col>
      <el-col :span="20" offset="4">
        <club_activity_list></club_activity_list>
      </el-col>
    </el-row>
  </div>
</template>
<script>
  import ActivityList from '../../components/admin_club/ActivityList.vue'
  import JAside from '../../components/admin_club/ClubAside.vue'
  export default {
    components: {
      'club_aside': JAside,
      'club_activity_list': ActivityList
    },
    data () {
      return {}
    }
  }
</script>
<style>
</style>
