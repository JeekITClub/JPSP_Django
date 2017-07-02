<template>
  <div>
    <el-row class="tac">
      <el-col :span="4">
        <cd_aside></cd_aside>
      </el-col>
      <el-col :span="20" offset="4">
        <recruit_classroom_list type="Unconfirmed"></recruit_classroom_list>
      </el-col>
    </el-row>
  </div>
</template>
<script>
  import CDAside from '../../components/admin_cd/CDAside.vue'
  import RecruitClassroomList from '../../components/public/RecruitClassroomList.vue'
  export default {
    components: {
      'cd_aside': CDAside,
      'recruit_classroom_list': RecruitClassroomList
    }
  }
</script>
<style>
</style>
