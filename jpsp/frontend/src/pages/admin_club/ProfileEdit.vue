<template>
  <div>
    <div v-if="Authenticate===true">
      <el-row gutter="20">
        <el-col :span="4">
          <club_aside></club_aside>
        </el-col>
        <el-col :span="20">
          <club_profile_edit></club_profile_edit>
        </el-col>
      </el-row>
    </div>
    <div v-if="Authenticate===false || Authenticate===null">
      <p>未登陆</p>
    </div>
  </div>
</template>
<script>
  import JAside from '../../components/admin_club/ClubAside.vue'
  import ProfileEdit from '../../components/admin_club/ProfileEdit.vue'
  export default {
    name: 'ProfileEdit',
    components: {
      'club_aside': JAside,
      'club_profile_edit': ProfileEdit
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
  @import url("//unpkg.com/element-ui@1.3.2/lib/theme-default/index.css");
</style>
