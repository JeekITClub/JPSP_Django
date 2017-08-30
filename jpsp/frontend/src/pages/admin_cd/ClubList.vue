<template>
  <el-tabs v-model="TabsValue">
    <el-tab-pane label="已建立社团" name="Confirmed">
      <club_list type="confirmed" user=""></club_list>
    </el-tab-pane>
    <el-tab-pane label="未确认社团" name="Unconfirmed">
      <club_list type="unconfirmed" user=""></club_list>
    </el-tab-pane>
  </el-tabs>
</template>
<script>
  import ClubList from '../../components/public/ClubList.vue'

  export default {
    components: {
      'club_list': ClubList
    },
    data () {
      return {
        TabsValue: 'Unconfirmed'
      }
    }
  }
</script>
<style>
</style>
