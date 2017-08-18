<template>
  <div class="card">
    <div class="card-image">
      <img src="../../assets/dp.jpg" class="image">
    </div>

    <div class="card-content">
      <div class="content">
        <h3 class="name" v-if="Club.IfRecruit === 'True'">{{ Club.ClubName }}</h3>
        <h3 class="name" v-if="Club.IfRecruit === 'False'">{{ Club.ClubName }}(不招新)</h3>
      </div>
      <footer class="card-footer">
        <router-link :to="{ name: 'ClubIndex', params: { ClubId:Club.ClubId, Club:Club }}" class="attend-club">
          <a class="button is-primary" v-if="Club.IfRecruit === 'True'">我想加入</a>
          <a class="button is-primary" v-else-if="Club.IfRecruit === 'False'">查看该社团</a>
        </router-link>
      </footer>
    </div>
  </div>
</template>
<script>
  export default {
    data () {
      return {}
    },
    props: {
      Club: {}
    },
    computed: {
      /**
       * @return {string}
       */
      GetApi () {
        return this.$store.state.Api
      }
    }
  }
</script>
<style scoped>
  .attend-club {
    margin-top: 5px;
  }
</style>
