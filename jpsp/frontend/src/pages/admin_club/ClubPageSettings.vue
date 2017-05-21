<template>
  <div>
    <el-row class="tac">
      <el-col :span="4">
        <club_aside></club_aside>
      </el-col>
      <el-col :span="20" offset="4">
        <club_page_settings></club_page_settings>
      </el-col>
    </el-row>
    <JFooter></JFooter>
  </div>
</template>
<script>
  import ClubPageSettings from '../../components/admin_club/ClubPageSettings.vue'
  import ClubAside from '../../components/admin_club/ClubAside.vue'
  import JFooter from '../../components/public/JFooter.vue'
  export default {
    components: {
      'club_aside': ClubAside,
      'club_page_settings': ClubPageSettings,
      'JFooter': JFooter
    }
  }
</script>
<style>
</style>
