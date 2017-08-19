<template>
  <div class="card">
    <div class="card-image">
      <figure class="image is-1by1">
      <img src="../../assets/dp.jpg">
      </figure>
    </div>

    <div class="card-content">
      <div class="content">
        <h3 class="" v-if="Club.IfRecruit === 'True'">{{ Club.ClubName }}</h3>
        <h3 class="" v-if="Club.IfRecruit === 'False'">{{ Club.ClubName }}(不招新)</h3>
      </div>
    </div>
      <footer class="card-footer">
        <router-link :to="{ name: 'ClubIndex', params: { ClubId:Club.ClubId, Club:Club }}" class="card-footer-item">
          <p v-if="Club.IfRecruit === 'True'">我想加入</p>
          <p v-else-if="Club.IfRecruit === 'False'">查看该社团</p>
        </router-link>
      </footer>
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
</style>
