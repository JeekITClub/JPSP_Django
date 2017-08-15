<template>
  <div>
    <div class="container">
      <div class="row">
      <div class="col-sm-6 col-md-4" v-for="club in ClubList">
        <club-show :club=club></club-show>
      </div>
      </div>
      <div class="row">
        <el-pagination
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          :current-page.sync="currentPage1"
          :page-size="100"
          layout="total, prev, pager, next"
          :total="1000" align="center">
        </el-pagination>
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
            ClubName: 'jeek',
            ClubId: '233',
            IfRecruit: 'True'
          },
          {
            ClubName: 'jeek',
            ClubId: '233',
            IfRecruit: 'True'
          },
          {
            ClubName: 'jeek',
            ClubId: '233',
            IfRecruit: 'True'
          },
          {
            ClubName: 'jeek',
            ClubId: '233',
            IfRecruit: 'True'
          },
          {
            ClubName: 'jeek',
            ClubId: '233',
            IfRecruit: 'True'
          },
          {
            ClubName: 'jeek',
            ClubId: '233',
            IfRecruit: 'True'
          },
          {
            ClubName: 'jeek',
            ClubId: '233',
            IfRecruit: 'True'
          },
          {
            ClubName: 'jeek',
            ClubId: '233',
            IfRecruit: 'True'
          },
          {
            ClubName: 'jeek',
            ClubId: '233',
            IfRecruit: 'True'
          },
          {
            ClubName: 'jeek',
            ClubId: '233',
            IfRecruit: 'True'
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
