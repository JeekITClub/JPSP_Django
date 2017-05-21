<template>
  <div>
    <el-row class="tac">
      <el-col :span="4">
        <cd_aside></cd_aside>
      </el-col>
      <el-col :span="20" offset="4">
        <club_recruit_classroom_list></club_recruit_classroom_list>
      </el-col>
    </el-row>
  </div>
</template>
<script>
  import CDAside from '../../components/admin_cd/CDAside.vue'
  import RecruitClassroomList from '../../components/admin_cd/RecruitClassroomList.vue'
  export default {
    components: {
      'cd_aside': CDAside,
      'club_recruit_classroom_list': RecruitClassroomList
    }
  }
</script>
<style>
</style>
