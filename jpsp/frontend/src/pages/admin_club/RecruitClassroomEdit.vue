<template>
  <club_recruit_classroom_apply></club_recruit_classroom_apply>
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
