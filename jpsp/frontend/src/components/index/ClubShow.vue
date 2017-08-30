<template>
  <div class="card">
    <div class="card-image">
      <figure class="image is-1by1">
      <img src="../../assets/dp.jpg">
      </figure>
    </div>

    <div class="card-content">
      <div class="content">
        <p class="title is-4" v-if="Club.IfRecruit === 1">{{ Club.ClubName }}</p>
        <p class="title is-4" v-if="Club.IfRecruit === 0">{{ Club.ClubName }}(不招新)</p>
      </div>
    </div>
      <footer class="card-footer">
        <router-link :to="{ name: 'ClubIndex', params: { ClubId:Club.ClubId, Club:Club }}" class="card-footer-item">
          <p v-if="Club.IfRecruit === 1">我想加入</p>
          <p v-else-if="Club.IfRecruit === 0">查看该社团</p>
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
