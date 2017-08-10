<template>
  <div class="thumbnail">
    <img src="../../assets/1.jpg" class="logo">
    <div class="caption">
      <h3 class="name" v-if="Club.IfRecruit === 'True'">{{ Club.ClubName }}</h3>
      <h3 class="name" v-if="Club.IfRecruit === 'False'">{{ Club.ClubName }}(不招新)</h3>
      <p>
        <router-link :to="{ name: 'ClubIndex', params: { ClubId:Club.ClubId, Club:Club }}">
          <button class="btn btn-primary" type="button" v-if="Club.IfRecruit === 'True'">我想加入</button>
          <button class="btn btn-warning" type="button" v-else-if="Club.IfRecruit === 'False'">查看该社团</button>
        </router-link>
      </p>
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
  .name {
    padding-top: 10px;
  }
</style>
