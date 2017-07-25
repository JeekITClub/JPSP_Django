<template>
  <club_activity_apply></club_activity_apply>
</template>
<script>
  import ActivityApply from '../../components/admin_club/ActivityApply.vue'
  export default {
    name: 'ActivityApply',
    components: {
      'club_activity_apply': ActivityApply
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
