<template>
  <div>
    <div align="right">
      <el-button align="right" type="primary" size="big" @click="GoToEventForm()">添加社团事件</el-button>
    </div>
    <el-tabs v-model="TabsValue" type="card">
      <el-tab-pane label="所有" name="All">
        <event-list></event-list>
      </el-tab-pane>
      <el-tab-pane label="已审核" name="Confirmed">
        <event-list></event-list>
      </el-tab-pane>
      <el-tab-pane label="未审核" name="Unconfirmed">
        <event-list></event-list>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>
<script>
  import EventList from '../../components/public/EventList.vue'
  export default {
    components: {
      'EventList': EventList
    },
    data () {
      return {
        TabsValue: 'Confirmed'
      }
    },
    methods: {
      GoToEventForm () {
        this.$router.push('/event/form')
      }
    }
  }
</script>
<style>
</style>
