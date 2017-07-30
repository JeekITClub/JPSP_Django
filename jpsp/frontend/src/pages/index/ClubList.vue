<template>
  <div>
    <div align="right">
      <el-button @click="GoToEstablishClub" type="primary" size="big">
        建立社团
      </el-button>
    </div>
    <club_list user="Student" type="Established"></club_list>
  </div>
</template>
<script>
  import ClubList from '../../components/public/ClubList.vue'
  export default {
    components: {
      'club_list': ClubList
    },
    methods: {
      GoToEstablishClub () {
        this.$router.push('/club/establish')
      }
    }
  }
</script>
<style>
</style>
