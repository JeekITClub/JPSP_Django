<template>
  <div>
    <el-row class="tac">
      <el-col :span="20" offset="4">
        <club_recruit_classroom_list></club_recruit_classroom_list>
      </el-col>
    </el-row>
  </div>
</template>
<script>
  import RecruitClassroomList from '../../components/Public/RecruitClassroomList.vue'
  export default {
    components: {
      'club_recruit_classroom_list': RecruitClassroomList
    }
  }
</script>
<style>
</style>
