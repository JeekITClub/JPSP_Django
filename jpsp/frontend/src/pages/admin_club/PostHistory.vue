<template>
  <div>
    <div v-if="Authenticate===true">
      <el-row class="tac">
        <el-col span="4">
          <club_aside></club_aside>
        </el-col>
        <el-col span="20" offset="4">
          <club_post_history></club_post_history>
        </el-col>
      </el-row>
    </div>
    <div v-if="Authenticate===false || Authenticate===null">
      <p>未登陆</p>
    </div>
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
    },
    computed: {
      Authenticate () {
        return this.$store.state.Authenticated
      },
      GetClubName () {
        return this.$store.state.UserName
      },
      GetClubId () {
        return this.$store.state.ClubId
      },
      GetToken () {
        return this.$store.state.Token
      }
    }
  }
</script>
<style>
</style>
