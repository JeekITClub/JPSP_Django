<template>
  <el-table :data="Members" stripe>
    <el-table-column type="expand">
      <template scope="props">
        <el-form inline class="demo-table-expand">
          <div class="columns">
            <div class="column">
              <el-form-item label="QQ号">
                <span>{{ props.row.QQ }}</span>
              </el-form-item>
            </div>
          </div>
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
        <button class="button is-primary" @click="deleteMember(scope.row.UserId)">删除成员</button>
      </template>
    </el-table-column>
    <el-table-column label="操作" v-if="this.Type === 'Unconfirmed'">
      <template scope="scope">
        <button class="button is-primary" @click="confirmMember(scope.row.UserId)">添加成员</button>
      </template>
    </el-table-column>
  </el-table>
</template>
<script>
  import axios from 'axios'
  import Qs from 'qs'

  export default {
    data () {
      return {
        Members: [{}]
      }
    },
    props: {
      Type: {
        'default': 'Confirmed'
      }
    },
    methods: {
      deleteMember (member) {
        axios({
          method: 'DELETE',
          url: this.GetApi + 'clubships',
          data: Qs.stringify({
            UserId: null,
            ClubId: this.GetClubId,
            Token: this.GetToken
          })
        })
          .then(function (response) {
            if (response.data.message === 'success') {
              this.$notify.success({
                'title': 'success',
                'message': 'success'
              })
            } else if (response.data.message === 'error') {
              this.$notify.error({
                'title': 'error',
                'message': 'error'
              })
            }
          }.bind(this))
      },
      confirmMember (member) {
        axios({
          method: 'PUT',
          url: this.GetApi + 'clubships',
          data: Qs.stringfy({
            UserId: null,
            ClubId: this.GetClubId,
            Token: this.GetToken
          })
        })
          .then(function (response) {
            if (response.data.message === 'success') {
              this.$notify.success({
                'title': 'success',
                'message': 'success'
              })
            }
          }.bind(this))
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
      /**
       * @return {string}
       */
      GetApi () {
        return this.$store.state.Api
      }
    },
    mounted: function () {
      axios({
        method: 'PATCH',
        url: this.GetApi + 'clubships/' + this.$props.Type,
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
      }.bind(this))
    }
  }
</script>
<style>
</style>
