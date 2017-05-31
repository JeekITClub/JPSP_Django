<template>
  <div>
    <el-row class="tac">
      <el-col :span="4">
        <club_aside></club_aside>
      </el-col>
      <el-col :span="4" offset="20">
        <club_member_management></club_member_management>
      </el-col>
    </el-row>
    <JFooter></JFooter>
  </div>
</template>
<script>
  import ClubAside from '../../components/admin_club/ClubAside.vue'
  import JFooter from '../../components/admin_club/JFooter.vue'
  import MemberManagement from '../../components/admin_club/MemberManagement.vue'
  export default {
    name: 'MemberManagement',
    components: {
      'club_aside': ClubAside,
      'club_member_management': MemberManagement,
      'JFooter': JFooter
    }
  }
</script>
<style>
</style>
