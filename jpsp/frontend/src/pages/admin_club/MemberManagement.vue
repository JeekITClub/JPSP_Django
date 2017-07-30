<template>
  <div>
    <el-tabs v-model="TabsValue" type="card">
      <el-tab-pane name="All" label="所有">
        <member-management Type="All"></member-management>
      </el-tab-pane>
      <el-tab-pane name="Confirmed" label="已加入社员">
        <member-management Type="Confirmed"></member-management>
      </el-tab-pane>
      <el-tab-pane name="Unconfirmed" label="未确认社员">
        <member-management Type="Unconfirmed"></member-management>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>
<script>
  import MemberManagement from '../../components/admin_club/MemberManagement.vue'
  export default {
    components: {
      'MemberManagement': MemberManagement
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
