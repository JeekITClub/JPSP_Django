<template>
  <el-table :data="EventListTable">
    <el-table-column type="expand">
      <template scope="props">
        <el-form inline class="demo-table-expand">
          <el-form-item label="事件内容">
            <span>{{ props.row.Content }}</span>
          </el-form-item>
        </el-form>
      </template>
    </el-table-column>
    <el-table-column prop="Name" label="">
    </el-table-column>
    <el-table-column prop="Datetime" label=""></el-table-column>
  </el-table>
</template>
<script>
  import { getCookie } from 'tiny-cookie'
  import axios from 'axios'
  export default {
    data () {
      return {
        EventListTable: []
      }
    },
    props: {
      ClubId: {
        'default': ''
      }
    },
    computed: {
      GetUserId () {
        return getCookie('UserId')
      },
      GetAPI () {
          return this.$store.state.API
      }
    },
    methods: {},
    mounted: function () {
      axios({
        method: 'POST',
        url: this.GetAPI + '/event/list',
        data: JSON.stringify({
          ClubId: this.ClubId,
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
