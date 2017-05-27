<template>
  <div>
    <el-row class="tac">
      <el-col :span="24">
        <club_establish></club_establish>
      </el-col>
    </el-row>
  </div>
</template>
<script>
  import EstablishClub from '../../components/admin_club/EstablishClub.vue'
  export default {
    components: {
      'club_establish': EstablishClub
    },
    data () {
      return {}
    }
  }
</script>
<style>
</style>
