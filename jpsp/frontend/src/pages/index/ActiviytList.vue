<template>
  <div>
    <el-tabs v-model="TabsValue" type="card">
      <el-tab-pane label="未来活动" name="Future">
        <activity_list type="future" user="Student"></activity_list>
      </el-tab-pane>
      <el-tab-pane label="正在进行" name="Now">
        <activity_list type="now" user="Student"></activity_list>
      </el-tab-pane>
      <el-tab-pane label="已经结束" name="Stared">
        <activity_list type="past" user="Student"></activity_list>
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
    methods: {}
  }
</script>
<style>
</style>
