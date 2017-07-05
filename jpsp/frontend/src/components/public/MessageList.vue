<template>
  <el-table :data=MessageListTable>
    <el-table-column type="expand">
      <template scope="props">
        <el-form inline class="demo-table-expand">
          <el-row class="tac">
            <el-col :span="24">
              <el-form-item label="消息内容">
                <span>{{ props.row.Content }}</span>
              </el-form-item>
            </el-col>
          </el-row>
        </el-form>
      </template>
    </el-table-column>
    <el-table-column prop="FromUser" label="发送用户">
    </el-table-column>
    <el-table-column prop="ToUser" label="接受用户">
    </el-table-column>
    <el-table-column prop="Date" label="日期">
    </el-table-column>
    <el-table-column label="操作" v-if=" type === 'Unread'">
      <template scope="scope">
        <el-button size="small" type="success" @click="ReadSubmit(scope.row.pk)">
          标为已阅
        </el-button>
      </template>
    </el-table-column>
  </el-table>
</template>
<script>
  import axios from 'axios'
  export default {
    data () {
      return {}
    },
    props: {
      type: {
        'default': 'Unread'
      },
      user: {
        'default': 'Club'
      }
    },
    methods: {
      ReadSubmit (pk) {
        axios({
          method: 'POST',
          url: '',
          data: JSON.stringify({
            Token: this.GetToken,
            Pk: pk
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
      },
      GetClubId () {
        return this.$store.state.ClubId
      }
    },
    mounted: function () {
      if (user === 'CD') {
        axios({
          method: 'POST',
          url: '',
          data: JSON.stringify({
            Token: this.GetToken,
            UserId: this.GetUserId
          })
        }).then(function (response) {
          if (response.data.message === 'error') {
            this.$notify.error({
              'title': '错误',
              'message': '无法获得数据'
            })
          }
        })
      } else if (user === 'Club') {
        axios({
          method: 'POST',
          url: '',
          data: JSON.stringify({
            Token: this.GetToken,
            ClubId: this.GetClubId
          })
        }).then(function (response) {
          if (response.data.message === 'error') {
            this.$notify.error({
              'title': '错误',
              'message': '无法获得数据'
            })
          }
        })
      }
    }
  }
</script>
<style>
</style>
