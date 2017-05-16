<template>
  <div>
    <el-row>
      <el-col :span="4">
        <club_aside></club_aside>
      </el-col>
      <el-col :span="20">
        <club_profile_edit></club_profile_edit>
      </el-col>
    </el-row>
  </div>
</template>
<script>
  import JAside from '../../components/admin_club/JAside.vue'
  import ProfileEdit from '../../components/admin_club/ProfileEdit.vue'
  export default {
    name: 'ProfileEdit',
    components: {
      'club_aside': JAside,
      'club_profile_edit': ProfileEdit
    }
  }
</script>
<style>
  @import url("//unpkg.com/element-ui@1.3.2/lib/theme-default/index.css");
</style>
