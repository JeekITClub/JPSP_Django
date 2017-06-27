<template>
  <div>
    <el-tabs v-model="TabsValue" type="card">
      <el-tab-pane label="未来活动" name="Future">
        <cd_list type="future"></cd_list>
      </el-tab-pane>
      <el-tab-pane label="正在进行" name="Now">
        <cd_list type="now"></cd_list>
      </el-tab-pane>
      <el-tab-pane label="已经结束" name="Stared">
        <cd_list type="past"></cd_list>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>
<script>
  import ActivityList from '../../components/index/ActivityList.vue'
  export default {
    components: {
      'cd_list': ActivityList
    },
    data () {
      return {
        TabsValue: 'Future'
      }
    },
    methods: {}
  }
</script>
<style>
</style>
