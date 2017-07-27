<template>
  <club_profile_edit></club_profile_edit>
</template>
<script>
  import {getCookie} from 'tiny-cookie'
  import ProfileEdit from '../../components/admin_club/ProfileEdit.vue'
  export default {
    name: 'ProfileEdit',
    components: {
      'club_profile_edit': ProfileEdit
    },
    computed: {
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
