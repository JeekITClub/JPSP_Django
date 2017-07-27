<template>
  <el-table :data=ActivityFormTable>
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
  </el-table>
</template>

<script>
  import axios from 'axios'
  export default {
    data () {
      return {
        ActivityFormTable: [656, 89898]
      }
    },
    props: {
      user: {
        'default': 'Student'
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
          this.ActivityFormTable = JSON.parse(response.data.data)
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
