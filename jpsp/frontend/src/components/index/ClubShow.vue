<template>
  <div>
    <div class="logo">
      <img src="../../assets/1.jpg"></img>
    </div>
    <div class="name">
      <span><router-link :to="{ name: 'ClubIndex', params: { ClubId:Club.Id }}">
        {{ Club.Name }}
      </router-link></span>
    </div>
  </div>
</template>
<script>
  import axios from 'axios'
  export default {
    data () {
      return {
        Club: {
          Id: this.$props.id,
          Name: ''
        }
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
<style>

</style>
