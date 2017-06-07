<template>
  <div>
    <div v-if="Authenticate===true">
      <el-row class="tac">
        <el-col :span="4">
          <club_aside></club_aside>
        </el-col>
        <el-col :span="20" offset="20">
          <club_recruit_classroom_apply></club_recruit_classroom_apply>
        </el-col>
      </el-row>
    </div>
    <div v-if="Authenticate===false || Authenticate===null">
      <p>未登陆</p>
    </div>
  </div>
</template>
<script>
  import JAside from '../../components/admin_club/ClubAside.vue'
  import RecruitClassroomApply from '../../components/admin_club/RecruitClassroomEdit.vue'
  export default {
    name: 'RecruitClassroomApply',
    components: {
      'club_aside': JAside,
      'club_recruit_classroom_apply': RecruitClassroomApply
    },
    computed: {
      Authenticate () {
        return this.$store.state.Authenticated
      },
      GetClubName () {
        return this.$store.state.UserName
      },
      GetClubId () {
        return this.$store.state.ClubId
      },
      GetToken () {
        return this.$store.state.Token
      }
    }
  }
</script>
<style>
</style>
