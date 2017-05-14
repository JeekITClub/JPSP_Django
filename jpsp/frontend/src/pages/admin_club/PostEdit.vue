<template>
  <club_Aside></club_Aside>
  <club_-post-edit></club_-post-edit>
</template>
<script>
  import Aside from '../../components/admin_club/Aside.vue'
  import PostEdit from '../../components/admin_club/PostEdit.vue'
  export default {
    name: 'PostEdit',
    components: {
      'club_Aside': Aside,
      'club_PostEdit': PostEdit
    }
  }
</script>
<style>
  @import url("//unpkg.com/element-ui@1.3.2/lib/theme-default/index.css");
</style>
