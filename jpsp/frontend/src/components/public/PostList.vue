<template>
  <div>
    <el-table :data=PostListTable>
      <el-table-column type="expand">
        <template scope="props">
          <div class="columns is-multiline">
            <div class="column">
              <el-form-item label="活动内容">
                <span>{{ props.row.Content }}</span>
              </el-form-item>
            </div>
            <div class="column">
              <el-form-item label="活动过程">
                <span>{{ props.row.Process }}</span>
              </el-form-item>
            </div>
            <div class="column">
              <el-form-item label="活动评价">
                <span>{{ props.row.Assessment }}</span>
              </el-form-item>
            </div>
            <div class="column">
              <el-form-item label="感悟分析">
                <span>{{ props.row.Feeling }}</span>
              </el-form-item>
            </div>
          </div>
        </template>
      </el-table-column>
      <el-table-column prop="ClubName" label="社团名称">
      </el-table-column>
      <el-table-column prop="LinkmanName" label="联系人">
      </el-table-column>
      <el-table-column prop="Date1" label="社团活动日期">
      </el-table-column>
      <el-table-column prop="Date2" label="社团活动时间">
      </el-table-column>
      <el-table-column prop="Region" label="活动地点">
      </el-table-column>
      <el-table-column prop="Stars" label="评价">
      </el-table-column>
      <el-table-column label="评价" v-if="user === 'CD' ">
        <template scope="scope">
          <el-rate v-on:change="StarSubmit(scope.row.pk, scope.row.Stars)" v-model="scope.row.Stars"></el-rate>
        </template>
      </el-table-column>
      <el-table-column label="操作" v-if="user === 'CD' && type != 'UnPassed'">
        <template scope="scope">
          <el-button size="small" type="danger" @click="DenySubmit(scope.row.pk)">
            拒绝
          </el-button>
        </template>
      </el-table-column>
      <el-table-column label="操作" v-if="user === 'CD' && type === 'UnPassed'">
        <template scope="scope">
          <el-button size="small" type="danger" @click="UndoDenySubmit(scope.row.pk)">
            撤销拒绝
          </el-button>
        </template>
      </el-table-column>
    </el-table>
    <div class="column">
    <!--TODO: pagination-->
      <el-pagination
        @current-change="handleCurrentChange"
        :current-page.sync="currentPage1"
        :page-size="10"
        layout="total, prev, pager, next"
        :total="1000">
      </el-pagination>
    </div>
  </div>
</template>

<script>
  import axios from 'axios'
  import Qs from 'qs'

  export default {
    data () {
      return {
        PostListTable: []
      }
    },
    props: {
      type: {
        'default': 'UnStared'
      },
      user: {
        'default': 'Club'
      }
    },
    methods: {
      StarSubmit (postid, star) {
        axios({
          method: 'POST',
          url: this.GetApi + 'post/star',
          data: Qs.stringify({
            Stars: star,
            PostId: postid,
            Token: this.GetToken
          }),
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
          }
        })
          .then(function (response) {
            if (response.data.message === 'success') {
              this.$notify({
                title: '成功',
                message: '成功评价社团活动 Id:' + postid,
                type: 'success'
              })
            } else {
              this.$notify.error({
                title: '错误',
                message: '无法评价社团活动'
              })
            }
          }.bind(this))
      },
      DenySubmit (postid) {
        axios({
          method: 'POST',
          url: this.GetApi + '/post/operate',
          data: Qs.stringify({
            PostId: postid,
            Token: this.GetToken,
            Operation: 'Deny'
          }),
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
          }
        }).then(function (response) {
          if (response.data.message === 'success') {
            this.$notify({
              title: '成功',
              message: '成功拒绝社团活动 Id:' + postid,
              type: 'success'
            })
          } else {
            this.$notify.error({
              title: '错误',
              message: '无法拒绝社团活动'
            })
          }
        }.bind(this))
      },
      UndoDenySubmit (postid) {
        axios({
          method: 'POST',
          url: this.GetApi + 'post/operate',
          data: Qs.stringify({
            PostId: postid,
            Token: this.GetToken,
            Operation: 'UndoDeny'
          }),
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
          }
        })
          .then(function (response) {
            if (response.data.message === 'success') {
              this.$notify({
                title: '成功',
                message: '成功撤销拒绝社团活动 Id:' + postid,
                type: 'success'
              })
            } else {
              this.$notify.error({
                title: '错误',
                message: '无法撤销拒绝社团活动'
              })
            }
          }.bind(this))
      }
    },
    computed: {
      GetUserId () {
        return this.$cookie.get('CDUserId')
      },
      GetCDToken () {
        return this.$cookie.get('CDToken')
      },
      /**
       * @return {string}
       */
      GetApi () {
        return this.$store.state.Api
      }
    },
    mounted: function () {
      if (this.user === 'CD') {
        axios({
          method: 'POST',
          url: this.GetApi() + 'post/list',
          data: Qs.stringify({
            Type: this.type,
            Token: this.GetCDToken
          }),
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
          }
        })
          .then(function (response) {
            if (response.data.message === 'success') {
              this.PostListTable = JSON.parse(response.data.data)
            } else {
              this.$notify.error({
                title: '错误',
                message: '无法获得数据'
              })
            }
          }.bind(this))
      }
    }
  }
//      } else if (this.user === 'Club') {
//        axios({
//          method: 'POST',
//          url: this.GetApi + 'post/list',
//          data: Qs.stringify({
//            Type: this.type,
//            Token: this.GetClubToken,
//            ClubId: this.GetClubId
//          }),
//          headers: {
//            'Content-Type': 'application/x-www-form-urlencoded'
//          }
//        })
//          .then(function (response) {
//            if (response.data.message === 'success') {
//              this.PostListTable = JSON.parse(response.data.data)
//            } else {
//              this.$notify.error({
//                title: '错误',
//                message: '无法获得数据'
//              })
//            }
//          }.bind(this))

</script>
<style scoped>
  @import '../../assets/el-page.css';
</style>
