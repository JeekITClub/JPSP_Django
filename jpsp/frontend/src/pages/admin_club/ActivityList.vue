<template>
  <div>
    <div align="right">
      <el-button @click="GoToActivityForm" type="primary" size="big">申请活动</el-button>
    </div>
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
  </div>
</template>
<script>
  import ActivityList from '../../components/public/ActivityList.vue'
  export default {
    components: {
      'activity_list': ActivityList
    },
    data () {
      return {
        TabsValue: 'Now'
      }
    },
    methods: {
      GoToActivityForm () {
        this.$router.push('/activity/form')
      }
    }
  }
</script>
<style>
</style>
