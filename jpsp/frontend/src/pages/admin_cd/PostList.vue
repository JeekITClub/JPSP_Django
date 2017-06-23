<template>
  <div>
    <cd_post_list></cd_post_list>
  </div>
</template>
<script>
  import PostList from '../../components/admin_cd/PostList.vue'
  import CDAside from '../../components/admin_cd/CDAside.vue'
  export default {
    components: {
      'cd_aside': CDAside,
      'cd_post_list': PostList
    },
    data () {
      return {}
    }
  }
</script>
<style>
</style>
