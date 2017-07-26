<template>
  <div>

  </div>
</template>
<script>
  import ClubPageSettings from '../../components/admin_club/ClubPageSettings.vue'
  import ClubAside from '../../components/admin_club/ClubAside.vue'
  export default {
    components: {
      'club_aside': ClubAside,
      'club_page_settings': ClubPageSettings
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
