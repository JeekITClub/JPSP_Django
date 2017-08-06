<template>
  <div>
    <div class="container">
      <div class="col-sm-6 col-md-4" v-for="Club in ClubList">
        <club-show :club=Club></club-show>
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
        ClubList: [
          {
            ClubId: '1',
            ClubName: 'Jeek',
            Introduction: '233333333'
          },
          {
            ClubId: '2',
            ClubName: 'JTV',
            Introduction: '23333333333'
          },
          {
            ClubId: '3',
            ClubName: '???',
            Introduction: '2333333333333'
          }
        ]
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
        method: 'POST',
        url: this.GetApi + 'clublist',
        data: JSON.stringify({
          Token: '',
          Type: 'Established'
        })
      }).then(function (response) {
        if (response.data.message === 'success') {
          this.ClubList = JSON.parse(response.data.data)
        } else {
          console.log('get club list error')
        }
      }.bind(this))
    }
  }
</script>
<style>
</style>
