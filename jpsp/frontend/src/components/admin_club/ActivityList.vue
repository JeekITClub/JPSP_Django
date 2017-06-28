<template>
  <div>

    <el-dialog title="收货地址" :visible.sync="dialogTableVisible">

    </el-dialog>
  </div>
</template>

<script>
  import axios from 'axios'
  export default {
    data () {
      return {
        ActivityListTable: [],
        dialogTableVisible: false
      }
    },
    methods: {
      HandleDeleteSubmit (index, row) {
        axios({
          method: 'POST',
          url: '/api/cd/Post/DeleteSubmit',
          data: JSON.stringify({
            HandleTime: '',
            // TODO: HandleTime
            PostId: '',
            // TODO: PostId
            Token: ''
          })
        })
      }
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
        url: 'http://127.0.0.1:8000/api/club/activity/list',
        data: JSON.stringify({
          Token: this.GetToken,
          Type: this.type
        })
      })
        .then(function (response) {
          if (response.data.message === 'success') {
            this.ActivityListTable = JSON.parse(response.data.data)
            console.log('success')
          } else {
            console.log('error')
          }
        }.bind(this))
    }
  }
</script>
