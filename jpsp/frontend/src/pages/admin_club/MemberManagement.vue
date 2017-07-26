<template>
  <div>
    <el-tabs v-model="TabsValue" type="card">
      <el-tab-pane label="所有" name="All">
        <club_member_management></club_member_management>
      </el-tab-pane>
      <el-tab-pane label="成员" name="Confirmed">
        <club_member_management></club_member_management>
      </el-tab-pane>
      <el-tab-pane label="未确认社员" name="Unconfirmed">
        <club_member_management></club_member_management>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>
<script>
  import MemberManagement from '@/pages/admin_club/MemberManagement.vue'
  export default {
    name: 'MemberManagement',
    components: {
      'club_member_management': MemberManagement
    },
    computed: {
      Authenticate () {
        return this.$store.state.Authenticated
      }
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
