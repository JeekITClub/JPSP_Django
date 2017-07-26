<template>
  <el-table :data="EventListTable">
    <el-table-column type="expand">
    </el-table-column>
    <el-table-column prop="" label="">
    </el-table-column>
  </el-table>
</template>
<script>
  import {getCookie} from 'tiny-cookie'
  import axios from 'axios'
  export default {
    data () {
      return {
        EventListTable: []
      }
    },
    props: {
      type: {
        'default': ''
      },
      user: {
        'default': ''
      }
    },
    computed: {
      GetUserId () {
        return getCookie('UserId')
      }
    },
    methods: {},
    mounted: function () {
      axios({
        method: 'POST',
        url: '',
        data: JSON.stringify({
          Type: this.type,
          Token: this.Token
        })
      }).then(function (response) {
        if (response.data.message === 'success') {
          this.EventListTable = JSON.parse(response.data.data)
        } else {
          this.$notify.error({
            title: '错误',
            message: '无法获得数据'
          })
        }
      }.bind(this))
    }
  }
</script>
<style>
</style>
