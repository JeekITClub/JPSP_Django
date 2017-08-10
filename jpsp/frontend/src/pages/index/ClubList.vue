<template>
  <div>
    <div align="right">
      <el-button @click="GoToEstablishClub" type="primary" size="big">
        建立社团
      </el-button>
    </div>
  </div>
</template>
<script>
  import ClubShow from '../../components/index/ClubShow.vue'
  export default {
    components: {
      'club_show': ClubShow
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
