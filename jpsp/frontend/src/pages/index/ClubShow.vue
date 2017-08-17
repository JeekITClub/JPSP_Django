<template>
  <div>
    <div class="container">
      <div class="row">
      <div class="col-sm-6 col-md-4" v-for="club in ClubList">
        <club-show :Club=club></club-show>
      </div>
      </div>
      <div class="row">
        <el-pagination
          @current-change="handleCurrentChange"
          :current-page.sync="currentPageData"
          :page-size="12"
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
            ClubId: '303',
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
        ],
        currentPageData: 1
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
        url: this.GetApi + 'club/show',
        params: {
          Page: 1
        }
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
    },
    methods: {
      handleCurrentChange () {
        axios({
          method: 'GET',
          url: this.GetApi + 'club/show',
          params: {
            Page: this.currentPageData
          }
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
  }
</script>
<style>
</style>
