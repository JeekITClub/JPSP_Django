<template>
  <div v-if="Authenticate===true">
    <el-row class="tac">
      <el-col :span="4">
        <club_aside></club_aside>
      </el-col>
      <el-col :span="20">
        <club_recruit_member></club_recruit_member>
      </el-col>
    </el-row>
  </div>
</template>
<script>
  import JAside from '../../components/admin_club/ClubAside.vue'
  import RecruitMember from '../../components/admin_club/RecruitMember.vue'
  export default {
    components: {
      'club_aside': JAside,
      'club_recruit_member': RecruitMember
    },
    computed: {
      Authenticate () {
        return this.$store.state.Authenticated
      }
    }
  }
</script>
<style>
</style>
