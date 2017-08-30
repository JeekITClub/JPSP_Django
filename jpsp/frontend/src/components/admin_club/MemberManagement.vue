<template>
  <el-table :data="Members" stripe>
    <el-table-column type="expand">
      <template scope="props">
        <el-form inline class="demo-table-expand">
          <el-row class="tac">
            <el-col :span="24">
              <el-form-item label="QQ号">
                <span>{{ props.row.QQ }}</span>
              </el-form-item>
            </el-col>
            <el-col :span="24" v-if="this.Type == 'Unconfirmed'">
              <el-form-item label="加入理由">
                <!--加入社团的理由-->
                <span>{{ props.row.Reason }}</span>
              </el-form-item>
            </el-col>
          </el-row>
        </el-form>
      </template>
    </el-table-column>
    <el-table-column prop="Name" label="姓名" width="">
    </el-table-column>
    <el-table-column prop="Grade" label="年级" width="">
    </el-table-column>
    <el-table-column prop="Class" label="班级" width="">
    </el-table-column>
    <el-table-column label="操作" v-if="this.Type === 'Confirmed'">
      <template scope="scope">
        <el-button @click="deleteMember(scope.row.UserId)" type="primary">删除成员</el-button>
      </template>
    </el-table-column>
    <el-table-column label="操作" v-if="this.Type === 'Unconfirmed'">
      <template scope="scope">
        <el-button @click="addMember(scope.row.UserId)" type="primary">添加成员
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
        Members: [
          {
            UserId: '1',
            Name: 'NCJ',
            Grade: '1',
            Class: '1',
            State: 'Confirmed',
            Reason: 'a'
          }
        ]
      }
    },
    props: {
      Type: {
        'default': 'Confirmed'
      }
    },
    methods: {
      addMember () {
        // TODO: addMember method
      },
      deleteMember (member) {
        console.log('success')
      }
    },
    computed: {
      GetClubName () {
        return this.$cookie.get('ClubName')
      },
      GetClubId () {
        return this.$cookie.get('ClubId')
      },
      GetToken () {
        return this.$cookie.get('ClubToken')
      },
      GetApi () {
        return this.$store.state.Api
      }
    },
    mounted: function () {
      axios({
        method: 'POST',
        url: this.GetApi + 'member',
        data: JSON.stringify({
          ClubId: this.GetClubId,
          Token: this.GetClubId,
          Type: this.Type
        }),
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        }
      }).then(function (response) {
        if (response.data.message === 'success') {
          this.Members = JSON.parse(response.data.data)
        } else {
          this.$notify.error({
            'title': '失败',
            'message': '获取数据失败'
          })
        }
      })
    }
  }
</script>
<style>
</style>
