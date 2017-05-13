<template>
  <club_aside></club_aside>
</template>
<script>
  import Aside from '../../components/admin_club/Aside.vue'
  export default {
    name: 'PorfileEdit',
    components: {
      'club_aside': Aside
    }
  }
</script>
<style>
  @import url("//unpkg.com/element-ui@1.3.2/lib/theme-default/index.css");
</style>
