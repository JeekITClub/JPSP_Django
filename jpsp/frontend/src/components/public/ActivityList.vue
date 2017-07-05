<template>
  <el-table :data=ActivityListTable>
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
              <el-form-item label="活动地点">
                <span>{{ props.row.Region }}</span>
              </el-form-item>
            </el-col>
          </el-row>
        </el-form>
      </template>
    </el-table-column>
    <el-table-column prop="ActivityId" label="活动序号">
    </el-table-column>
    <el-table-column prop="Name" label="活动名称">
    </el-table-column>
    <el-table-column prop="ClubName" label="负责社团">
    </el-table-column>
    <el-table-column prop="Date1" label="开始日期">
    </el-table-column>
    <el-table-column prop="Date2" label="结束时间">
    </el-table-column>
    <el-table-column prop="State" label="状态">
      <template scope="scope">
        <span v-if="scope.row.State === '0'">未审核</span>
        <span v-if="scope.row.State === '1'" style="color: green">已审核</span>
        <span v-if="scope.row.State === '2'" style="color: red">被拒绝</span>
      </template>
    </el-table-column>
    <el-table-column label="操作" v-if="user === 'Student'">
      <template scope="scope">
        <el-button size="small" type="danger" @click="AttendSubmit(scope.row.pk)">
          加入活动
        </el-button>
      </template>
    </el-table-column>
    <el-table-column label="操作" v-if="user === 'Club' && type === 'Future' || type === 'All">
      <template scope="scope">
        <el-button size="small" type="danger" @click="CancelSubmit(scope.row.pk)">
          取消活动
        </el-button>
      </template>
    </el-table-column>
    <el-table-column label="操作" v-if="user === 'CD' && type != 'Unconfirmed' ">
      <template scope="scope">
        <el-button size="small" type="danger" @click="DenySubmit(scope.row.pk)">
          拒绝
        </el-button>
      </template>
    </el-table-column>
    <el-table-column label="操作" v-if="user === 'CD' && type == 'Unconfirmed' ">
      <template scope="scope">
        <el-button size="small" type="success" @click="ConfirmSubmit(scope.row.pk)">
          同意
        </el-button>
      </template>
    </el-table-column>
    <el-table-column label="操作" v-if="user === 'CD' && type != 'Denied' && type !='Unconfirmed'">
      <template scope="scope">
        <el-button size="small" type="success" @click="UndoDenySubmit(scope.row.pk)">
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
        ActivityListTable: []
      }
    },
    props: {
      type: {
        'default': 'UnStared'
      },
      user: {
        'default': 'Student'
      }
    },
    methods: {
      DenySubmit (ActivityId) {
        axios({
          method: 'POST',
          url: 'http://127.0.0.1/api/activity/operate',
          data: JSON.stringify({
            ActivityId: ActivityId,
            Token: this.GetToken,
            Operation: 'Deny'
          })
        })
          .then(function (response) {
          if (response.data.message === 'success') {
            this.$notify({
              title: '成功',
              message: '成功拒绝活动' + ActivityId,
              type: 'success'
            })
          } else if (response.data.message === 'error') {
            this.$notify.error({
              title: '错误',
              message: '拒绝活动' + ActivityId + '失败'
            })
          }
        }.bind(this))
      },
      UndoDenySubmit (ActivityId) {
        axios({
          method: 'POST',
          url: 'http://127.0.0.1/api/activity/operate',
          data: JSON.stringify({
            ActivityId: ActivityId,
            Token: this.GetToken,
            Operation: 'UndoDeny'
          }.bind(this))
        }).then(function (response) {
          if (response.data.message === 'success') {
            this.$notify({
              title: '成功',
              message: '成功撤销拒绝活动' + ActivityId,
              type: 'success'
            })
          } else if (response.data.message === 'error') {
            this.$notify.error({
              title: '错误',
              message: '撤销拒绝活动' + ActivityId + '失败'
            })
          }
        }.bind(this))
      },
      AttendSubmit (ActivityId) {
        axios({
          method: 'POST',
          url: 'http://127.0.0.1/api/activity/attend',
          data: JSON.stringify(({
            ActivityId: ActivityId,
            Token: this.GetToken,
            StudentId: this.GetUserId
          }.bind(this)))
        }).then(function (response) {
          if (response.data.message === 'success') {
            this.$notify({
              title: '成功',
              message: '成功加入活动' + ActivityId,
              type: 'success'
            })
          } else if (response.data.message === 'error') {
            this.$notify.error({
              title: '错误',
              message: '加入活动' + ActivityId + '失败'
            })
          }
        }.bind(this))
      },
      CancelSubmit (ActivityId) {
        axios({
          method: 'POST',
          url: '',
          data: JSON.stringify({
            ActivityId: ActivityId,
            Token: this.GetToken
          }.bind(this))
        })
      },
      ConfirmSubmit (ActivityId) {
        axios({
          method: 'POST',
          url: 'http://127.0.0.1:8000/api/activity/operate',
          data: JSON.stringify({
            ActivityId: ActivityId,
            Token: this.GetToken,
            Operation: 'Confirm'
          })
        })
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
      },
      GetUserId () {
        return this.$store.state.UserId
      }
    },
    mounted: function () {
      axios({
        method: 'POST',
        url: 'http://127.0.0.1:8000/api/activity/list',
        data: JSON.stringify({
          Type: this.type,
          Token: this.GetToken
        })
      }).then(function (response) {
        if (response.data.message === 'success') {
          this.ActivityListTable = JSON.parse(response.data.data)
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
