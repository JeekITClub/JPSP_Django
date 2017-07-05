<template>
  <div>
    <el-tabs v-model="TabsValue" type="card">
      <el-tab-pane label="所有" name="All">
        <recruit_classroom_list type="All" user="Club"></recruit_classroom_list>
      </el-tab-pane>
      <el-tab-pane label="已审核" name="Confirmed">
        <recruit_classroom_list type="Confirmed" user="Club"></recruit_classroom_list>
      </el-tab-pane>
      <el-tab-pane label="未审核" name="Unconfirmed">
        <recruit_classroom_list type="Unconfirmed" user="Club"></recruit_classroom_list>
      </el-tab-pane>
      <el-tab-pane label="已拒绝" name="Denied">
        <recruit_classroom_list type="Denied" user="Club"></recruit_classroom_list>
      </el-tab-pane>
    </el-tabs>
    <recruit_classroom_list></recruit_classroom_list>
  </div>
</template>
<script>
  import RecruitClassroomList from '../../components/public/RecruitClassroomList.vue'
  export default {
    components: {
      'recruit_classroom_list': RecruitClassroomList
    },
    data: {
      TabsValue: 'Confirmed'
    }
  }
</script>
<style>
</style>
