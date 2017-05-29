<template>
  <div>
    <el-row class="tac">
      <el-col span="4">
        <club_aside></club_aside>
      </el-col>
      <el-col span="20" offset="4">
        <club_post_history></club_post_history>
      </el-col>
    </el-row>
  </div>
</template>
<script>
  import PostHistory from '../../components/admin_club/PostHistory.vue'
  import ClubAside from '../../components/admin_club/ClubAside.vue'
  export default {
    components: {
      'club_aside': ClubAside,
      'club_post_history': PostHistory
    },
    data () {
      return {}
    }
  }
</script>
<style>
</style>
