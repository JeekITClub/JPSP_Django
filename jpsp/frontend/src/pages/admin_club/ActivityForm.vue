<template>
  <div>
    <el-tabs v-model="TabsValue" type="card">
      <el-tab-pane label="所有" name="All">
        <club_activityform type="All" user="Club"></club_activityform>
      </el-tab-pane>
      <el-tab-pane label="审核中" name="Unconfirmed">
        <club_activityform type="Unconfirmed" user="Club"></club_activityform>
      </el-tab-pane>
      <el-tab-pane label="已通过" name="Confirmed">
        <club_activityform type="Confirmed" user="Club"></club_activityform>
      </el-tab-pane>
      <el-tab-pane label="被拒绝" name="Denied">
        <club_activityform type="Denied" user="Club"></club_activityform>
      </el-tab-pane>
      <el-tab-pane label="未来活动" name="Future">
        <club_activityform type="Future" user="Club"></club_activityform>
      </el-tab-pane>
      <el-tab-pane label="正在进行" name="Now">
        <club_activityform type="Now" user="Club"></club_activityform>
      </el-tab-pane>
      <el-tab-pane label="已经结束" name="Stared">
        <club_activityform type="Past" user="Club"></club_activityform>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>
<script>
  import ActivityForm from '../../components/admin_club/ActivityForm.vue'
  export default {
    components: {
      'club_activityform': ActivityForm
    },
    data () {
      return {
        TabsValue: 'Confirmed'
      }
    }
  }
</script>
<style>
</style>
