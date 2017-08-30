<template>
  <div>
    <div class="club-show">
      <div class="columns is-mobile" align="right">
        <div class="column">
          <router-link class="button is-primary is-large" to="/Establish" align="right">创建社团</router-link>
        </div>
      </div>
      <div class="columns is-multiline is-mobile">
        <div class="column is-one-quarter" v-for="club in ClubList">
          <club-show :Club=club></club-show>
        </div>
      </div>
      <div class="column">
        <el-pagination
          @current-change="handleCurrentChange"
          :current-page.sync="Page"
          :page-size="12"
          layout="total, prev, pager, next"
          :total="50" align="center">
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
        Type: 'Confirmed',
        Page: 1,
        ClubList: []
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
      // 获取已成立社团列表
      axios({
        method: 'GET',
        url: this.GetApi + 'clubs/list',
        params: {
          Page: this.Page
        }
      })
        .then(function (response) {
          if (response.data.message === 'success') {
            this.ClubList = response.data.data
          } else {
            this.$notify.error({
              'message': '无法获得社团列表',
              'title': 'Error'
            })
          }
        }.bind(this))
    },
    methods: {
      handleCurrentChange (val) {
        axios({
          method: 'GET',
          url: this.GetApi + 'clubs/list/',
          params: {
            Page: val
          }
        })
          .then(function (response) {
            if (response.data.message === 'success') {
              this.ClubList = response.data.ClubList
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
  @import "../../assets/el-page.css";

  .club-show {
    padding-top: 3%;
    padding-right: 3%;
    padding-left: 3%;
  }
</style>
