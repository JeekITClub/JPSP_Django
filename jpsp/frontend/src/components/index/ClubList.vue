<template>
  <div>
   <el-table
      :data="ClubListTable"
      style="width: 100%">
      <el-table-column
        prop="ClubId"
        label="社团ID"
        width="300">
      </el-table-column>
      <el-table-column
        prop="ClubName"
        label="社团名称"
        width="300">
        <template scope="scope">
        <router-link :to="{ name: 'ClubIndex', params: { ClubId:scope.row.ClubId, Club: scope.row }}">{{ scope.row.ClubName }}</router-link>
          </template>
      </el-table-column>
      <el-table-column
        prop="ShezhangName"
        label="现任社长">
      </el-table-column>
    </el-table>
    <br>
  </div>
</template>

<script>
  import axios from 'axios'
  export default {
    data () {
      return {
        ClubListTable: [
          {
            ClubId: '001',
            ClubName: 'Jeek',
            ShezhangName: 'Ncj'
          }
        ]
      }
    },
    mounted: function () {
      axios({
        method: 'POST',
        url: 'http://127.0.0.1:8000/api/public/club/list',
        data: JSON.stringify({
          Token: this.GetToken
        })
      }).then(function (response) {
        if (response.data.message === 'success') {
          this.ClubListTable = JSON.parse(response.data.data)
          console.log('success')
        } else {
          console.log('error')
        }
      }.bind(this))
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
    }
  }
</script>
<style>
  @import url("//unpkg.com/element-ui@1.3.2/lib/theme-default/index.css");
</style>
