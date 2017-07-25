<template>
  <div>
    <el-row class="tac" :gutter="20">
      <el-col :span="4">
        <club_aside></club_aside>
      </el-col>
      <el-col :span="20">
        <el-tabs v-model="TabsValue" type="card">
          <el-tab-pane label="所有" name="All">
            <activity_list type="All" user="Club"></activity_list>
          </el-tab-pane>
          <el-tab-pane label="审核中" name="Unconfirmed">
            <activity_list type="Unconfirmed" user="Club"></activity_list>
          </el-tab-pane>
          <el-tab-pane label="已通过" name="Confirmed">
            <activity_list type="Confirmed" user="Club"></activity_list>
          </el-tab-pane>
          <el-tab-pane label="被拒绝" name="Denied">
            <activity_list type="Denied" user="Club"></activity_list>
          </el-tab-pane>
          <el-tab-pane label="未来活动" name="Future">
            <activity_list type="Future" user="Club"></activity_list>
          </el-tab-pane>
          <el-tab-pane label="正在进行" name="Now">
            <activity_list type="Now" user="Club"></activity_list>
          </el-tab-pane>
          <el-tab-pane label="已经结束" name="Stared">
            <activity_list type="Past" user="Club"></activity_list>
          </el-tab-pane>
        </el-tabs>
      </el-col>
    </el-row>
  </div>
</template>
<script>
  import ActivityList from '../../components/public/ActivityList.vue'
  import JAside from '../../components/admin_club/ClubAside.vue'
  export default {
    components: {
      'club_aside': JAside,
      'activity_list': ActivityList
    },
    data () {
      return {
        TabsValue: 'All'
      }
    }
  }
</script>
<style>
</style>
