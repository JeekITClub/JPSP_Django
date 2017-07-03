<template>
  <div>
    <el-tabs v-model="TabsValue" type="card">
      <el-tab-pane label="未审核" name="Unconfirmed">
        <activity_list type="Unconfirmed" user="CD"></activity_list>
      </el-tab-pane>
      <el-tab-pane label="已审核" name="Confirmd">
        <activity_list type="Confirmed" user="CD"></activity_list>
      </el-tab-pane>
      <el-tab-pane label="未通过" name="Denied">
        <activity_list type="Denied" user="CD"></activity_list>
      </el-tab-pane>
      <el-tab-pane label="所有" name="All">
        <activity_list type="All" user="CD"></activity_list>
      </el-tab-pane>
      <el-tab-pane label="过期" name="Past">
        <activity_list type="Past" user="CD"></activity_list>
      </el-tab-pane>
      <el-tab-pane label="进行中" name="Happening">
        <activity_list type="Happening" user="CD"></activity_list>
      </el-tab-pane>
      <el-tab-pane label="未来" name="Future">
        <activity_list type="Future" user="CD"></activity_list>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>
<script>
  import CDAside from '../../components/admin_cd/CDAside.vue'
  import ActivityList from '../../components/public/ActivityList.vue'
  export default {
    components: {
      'cd_aside': CDAside,
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
