<template>
  <div class="container">
      <div class="col-sm-6 col-md-4" v-for="club in ClubList">
        <div class="thumbnail">
          <img src="../../assets/1.jpg">
          <div class="caption">
            <h3>{{ club.ClubName }}</h3>
            <p>{{ club.Introduction }}</p>
            <p><router-link :to="{ name: 'ClubIndex', params: { ClubId:club.ClubId }}"><button class="btn btn-primary" type="button">我想加入</button></router-link></p>
          </div>
        </div>
      </div>
  </div>
</template>
<script>
  import axios from 'axios'
  export default {
    data () {
      return {
        ClubList: [
          {
            ClubId: '12',
            ClubName: 'Jeek',
            Introduction: 'dadsadasdasdasdsaa'
          },
          {
            ClubId: '12',
            ClubName: 'Jeek',
            Introduction: 'dadsadasdasdasdsaa'
          },
          {
            ClubId: '12',
            ClubName: 'Jeek',
            Introduction: 'dadsadasdasdasdsaa'
          },
          {
            ClubId: '12',
            ClubName: 'Jeek',
            Introduction: 'dadsadasdasdasdsaa'
          },
          {
            ClubId: '12',
            ClubName: 'Jeek',
            Introduction: 'dadsadasdasdasdsaa'
          },
          {
            ClubId: '12',
            ClubName: 'Jeek',
            Introduction: 'dadsadasdasdasdsaa'
          }
        ]
      }
    },
    props: {
      id: {
        'default': '303'
      }
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
        url: this.GetApi + 'club'
      }).then(function (response) {
        if (response.data.message === 'success') {
          this.Club = JSON.parse(response.data.data)
        }
      }.bind(this))
    }
  }
</script>
<style scoped>
  @import '../../assets/index/css/bootstrap/bootstrap.min.css';
</style>
