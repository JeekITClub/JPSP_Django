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
        return this.$cookie.get('UserId')
      },
      GetIndexToken () {
        return this.$cookie.get('IndexToken')
      },
      GetUserName () {
        return this.$cookie.get('UserName')
      },
      GetIndexAuthenticated () {
        return this.$cookie.get('IndexAuthenticated')
      },
      /**
       * @return {string}
       */
      GetApi () {
        return this.$store.state.Api
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
        }),
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        }
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
