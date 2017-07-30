<template>
  <club_recruit_classroom_form></club_recruit_classroom_form>
</template>
<script>
  import {getCookie} from 'tiny-cookie'
  import RecruitClassroomForm from '../../components/admin_club/RecruitClassroomForm.vue'
  export default {
    name: 'RecruitClassroomApply',
    components: {
      'club_recruit_classroom_form': RecruitClassroomForm
    },
    computed: {
      GetClubName () {
        return getCookie('ClubName')
      },
      GetClubId () {
        return getCookie('ClubId')
      },
      GetToken () {
        return getCookie('ClubToken')
      }
    }
  }
</script>
<style>
</style>
