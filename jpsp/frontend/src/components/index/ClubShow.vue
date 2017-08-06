<template>
        <div class="thumbnail">
          <img src="../../assets/1.jpg" class="logo">
          <div class="caption">
            <h3 class="name">{{ Club.ClubName }}</h3>
            <p><router-link :to="{ name: 'ClubIndex', params: { ClubId:Club.ClubId, Club:Club }}"><button class="btn btn-primary" type="button">我想加入</button></router-link></p>
          </div>
        </div>
</template>
<script>
  export default {
    data () {
      return {
      }
    },
    props: {
      Club: {
      }
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
