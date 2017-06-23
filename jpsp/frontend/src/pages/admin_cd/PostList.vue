<template>
  <div>
    <cd_post_list></cd_post_list>
  </div>
</template>
<script>
  import PostList from '../../components/admin_cd/PostList.vue'
  export default {
    components: {
      'cd_post_list': PostList
    },
    data () {
      return {}
    }
  }
</script>
<style>
</style>
