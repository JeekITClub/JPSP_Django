<template>

</template>

<script>
  import axios from 'axios'
  export default {
    data () {
      return {
        PostListTable: []
      }
    },
    props: {
    },
    methods: {
    },
    computed: {
      Authenticate () {
        return this.$store.state.Authenticated
      },
      GetUserName () {
        return this.$store.state.UserName
      },
      GetToken () {
        return this.$store.state.Token
      }
    },
    mounted: function () {
      axios({
        method: 'POST',
        url: 'http://127.0.0.1:8000/api/cd/post/list',
        data: JSON.stringify({
          Token: this.GetToken
        })
      })
        .then(function (response) {
          if (response.data.message === 'success') {
            this.PostListTable = JSON.parse(response.data.data)
            console.log('success')
          } else {
            console.log('error')
          }
        }.bind(this))
    }
  }
</script>
