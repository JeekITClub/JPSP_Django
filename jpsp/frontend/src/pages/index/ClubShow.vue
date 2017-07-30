<template>
  <div>
    <club-show></club-show>
  </div>
</template>
<script>
  import ClubShow from '../../components/index/ClubShow.vue'
  // import axios from 'axios'
  export default {
    data () {
      return {
        Type: '',
        Page: '1'
      }
    },
    components: {
      'ClubShow': ClubShow
    }
  }
</script>
<style>
</style>
