<template>
  <el-table :data=PostListTable>
    <el-table-column type="expand">
      <template scope="props">
        <el-form inline class="demo-table-expand">
          <el-row class="tac">
            <el-col :span="24">
              <el-form-item label="活动内容">
                <span>{{ props.row.Content }}</span>
              </el-form-item>
            </el-col>
            <el-col :span="24">
              <el-form-item label="活动过程">
                <span>{{ props.row.Process }}</span>
              </el-form-item>
            </el-col>
            <el-col :span="24">
              <el-form-item label="活动评价">
                <span>{{ props.row.Assessment }}</span>
              </el-form-item>
            </el-col>
            <el-col :span="24">
              <el-form-item label="感悟分析">
                <span>{{ props.row.Feeling }}</span>
              </el-form-item>
            </el-col>
          </el-row>
        </el-form>
      </template>
    </el-table-column>
    <el-table-column prop="pk" label="PostId">
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
</template>

<script>
  import axios from 'axios'
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
          url: 'http://127.0.0.1:8000/api/post/star',
          data: JSON.stringify({
            Stars: star,
            PostId: postid,
            Token: this.GetToken
          }.bind(this))
        }).then(function (response) {
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
          url: 'http://127.0.0.1:8000/api/post/operate',
          data: JSON.stringify({
            PostId: postid,
            Token: this.GetToken,
            Operation: 'Deny'
          })
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
          url: 'http://127.0.0.1:8000/api/post/operate',
          data: JSON.stringify({
            PostId: postid,
            Token: this.GetToken,
            Operation: 'UndoDeny'
          })
        }).then(function (response) {
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
        url: 'http://127.0.0.1:8000/api/post/list',
        data: JSON.stringify({
          Type: this.type,
          Token: this.GetToken
        })
      }).then(function (response) {
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
</script>
