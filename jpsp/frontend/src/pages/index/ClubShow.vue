<template>
  <div>
    <div class="container">
      <div class="col-sm-6 col-md-4" v-for="club in ClubList">
        <club-show :club=club></club-show>
      </div>
    </div>
  </div>
</template>
<script>
  import ClubShow from '../../components/index/ClubShow.vue'
  import axios from 'axios'
  export default {
    data () {
      return {
        Type: '',
        Page: '1',
        ClubList: []
      }
    },
    components: {
      'ClubShow': ClubShow
    },
    computed: {
      /**
       * @return {string}
       */
      GetApi () {
        return this.$store.state.Api
      }
    },
    mounted: function () {
      axios({
        method: 'GET',
        url: this.GetApi + 'club/show'
      })
        .then(function (response) {
          if (response.data.message === 'success') {
            this.ClubList = JSON.parse(response.data.data)
          } else {
            this.$notify.error({
              'message': '无法获得社团列表',
              'title': 'Error'
            })
          }
        }.bind(this))
    }
  }
</script>
<style>
</style>
