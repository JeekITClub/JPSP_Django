<template>
  <div>
    <el-raw class="tac">
      <el-col :span="4">
        <club_aside></club_aside>
      </el-col>
      <el-col :span="20" offset="20">
        <club_recruit_classroom_apply></club_recruit_classroom_apply>
      </el-col>
    </el-raw>
  </div>
</template>
<script>
  import JAside from '../../components/admin_club/ClubAside.vue'
  import RecruitClassroomApply from '../../components/admin_club/RecruitClassroomEdit.vue'
  export default {
    name: 'RecruitClassroomApply',
    components: {
      'club_aside': JAside,
      'club_recruit_classroom_apply': RecruitClassroomApply
    }
  }
</script>
<style>
</style>
