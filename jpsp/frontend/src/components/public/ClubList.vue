<template>
  <div>
  <el-table :data="ClubList" stripe style="width: 100%">
    <el-table-column type="expand">
      <template scope="props">
        <el-form>
        <div class="columns is-multiline">
          <div class="column">
            <el-form-item label="招新QQ群">
              <span>{{ props.row.EnrollGroupQQ }}</span>
            </el-form-item>
          </div>
          <!--<div class="column">-->
            <!--<el-form-item label="社团邮箱">-->
              <!--<span>{{ props.row.Email }}</span>-->
            <!--</el-form-item>-->
          <!--</div>-->
          <div class="column">
            <el-form-item label="社团介绍">
              <span>{{ props.row.Introduction }}</span>
            </el-form-item>
          </div>
          <!--<div class="column">-->
            <!--<el-form-item label="成就">-->
              <!--<span>{{ props.row.Achievements }}</span>-->
            <!--</el-form-item>-->
          <!--</div>-->
        </div>
        </el-form>
      </template>
    </el-table-column>
    <el-table-column prop="ClubId" label="社团Id"></el-table-column>
    <el-table-column prop="ClubName" label="社团名称"></el-table-column>
    <el-table-column prop="ShezhangName" label="社长姓名"></el-table-column>
    <el-table-column prop="ShezhangGrade" label="社长年级"></el-table-column>
    <el-table-column prop="ShezhangClass" label="社长班级"></el-table-column>
    <el-table-column prop="ShezhangQQ" label="社长QQ"></el-table-column>
    <el-table-column prop="IfRecruit" label="是否招新"></el-table-column>
    <el-table-column prop="State" label="是否已通过"></el-table-column>
    <el-table-column prop="Stars" label="评分"></el-table-column>
  </el-table>
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
</template>

<script>
  import axios from 'axios'
  import Qs from 'qs'

  export default {
    data () {
      return {
        Page: 1,
        ClubList: []
      }
    },
    methods: {
      handleCurrentChange (val) {
        axios({
          method: 'POST',
          url: this.GetApi + 'clubs/list/' + this.$props.type,
          data: Qs.stringify({
            Token: this.GetToken,
            UserId: this.GetUserId,
            Page: val
          }),
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
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
    },
    props: {
      user: {
        'default': 'CD'
      },
      type: {
        'default': 'unconfirmed'
      }
    },
    mounted: function () {
      axios({
        method: 'POST',
        url: this.GetApi + 'clubs/list/' + this.$props.type,
        data: Qs.stringify({
          Token: this.GetToken,
          UserId: this.GetUserId,
          Page: this.Page
        }),
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        }
      })
        .then(function (response) {
          if (response.data.message === 'success') {
            this.ClubList = response.data.ClubList
            console.log('success')
          } else {
            console.log('error')
          }
        }.bind(this))
    },
    computed: {
      GetUserId () {
        return this.$cookie.get('CDUserId')
      },
      GetCDToken () {
        return this.$cookie.get('CDToken')
      },
      GetUserName () {
        return this.$cookie.get('CDUserName')
      },
      GetCDAuthenticated () {
        return this.$cookie.get('CDAuthenticated')
      },
      /**
       * @return {string}
       */
      GetApi () {
        return this.$store.state.Api
      }
    }
  }
</script>
<style>
</style>
