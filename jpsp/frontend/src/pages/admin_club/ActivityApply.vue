<template>
  <el-row class="tac">
    <el-col :span="4">
      <club_aside></club_aside>
    </el-col>
    <el-col :span="20">
     <club_activity_apply></club_activity_apply>
    </el-col>
  </el-row>
</template>
<script>
  import JAside from '../../components/admin_club/ClubAside.vue'
  import ActivityApply from '../../components/admin_club/ActivityApply.vue'
  export default {
    name: 'ActivityApply',
    components: {
      'club_aside': JAside,
      'club_activity_apply': ActivityApply
    }
  }
</script>
<style>
</style>
