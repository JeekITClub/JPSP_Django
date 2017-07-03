<template>
  <el-table :data=RecruitClassroomList>
    <el-table-column prop="pk" label="'Id">
    </el-table-column>
    <el-table-column prop="ClubName" label="社团名称">
    </el-table-column>
    <el-table-column prop="LinkmanName" label="联系人">>
    </el-table-column>
    <el-table-column prop="Date1" label="教室开始使用时间">
    </el-table-column>
    <el-table-column prop="Date2" label="教室结束使用时间">
    </el-table-column>
    <el-table-column v-if="user === 'CD' && type === 'Unconfirmed'" label="操作">
      <template scope="scope">
        <el-button size="small" type="danger" @click="DenyRequest(scope.row.pk)">拒绝该请求</el-button>
      </template>
    </el-table-column>
    <el-table-column v-if="user === 'CD' && type ==='Denied'" label="操作">
      <template scope="scope">
        <el-button size="small" type="success" @click="UndoDenyRequest(scope.row.pk)">撤销拒绝活动</el-button>
      </template>
    </el-table-column>
    <el-table-column v-if="user === 'CD' && type ===' Unconfirmed' " label="操作">
      <template scope="scope">
        <el-button size="small" type="danger" @click="ArrangeClassroom('1', scope.row.pk)">
        </el-button>
        <el-button size="small" type="danger" @click="ArrangeClassroom('2', scope.row.pk)">
        </el-button>
        <el-button size="small" type="danger" @click="ArrangeClassroom('3', scope.row.pk)">
        </el-button>
        <el-button size="small" type="danger" @click="ArrangeClassroom('4', scope.row.pk)">
        </el-button>
        <el-button size="small" type="danger" @click="ArrangeClassroom('5', scope.row.pk)">
        </el-button>
        <el-button size="small" type="danger" @click="ArrangeClassroom('6', scope.row.pk)">
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
        RecruitClassroomList: []
      }
    },
    props: {
      user: {
        'default': 'Club'
      },
      type: {
        'default': 'Unconfirmed'
      }

    },
    methods: {
      ArrangeClassroom (classroom, pk) {
        axios({
          method: 'POST',
          url: 'http://127.0.0.1/api/recruit/classroom/operate',
          data: JSON.stringify({
            Id: pk,
            Classroom: classroom,
            Type: 'Arrange'
          })
        })
      },
      DenyRequest (pk) {
        axios({
          method: 'POST',
          url: 'http://127.0.0.1/api/recruit/classroom/operate',
          data: JSON.stringify({
            Id: pk,
            Type: 'Deny'
          })
        })
      },
      UndoDenyRequest (pk) {
        axios({
          method: 'POST',
          url: 'http://127.0.0.1/api/api/recruit/classroom/operate',
          data: JSON.stringify({
            Id: pk,
            Type: 'UndoDeny'
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
      }
    },
    mounted: function () {
      axios({
          method: 'POST',
          url: 'http://127.0.0.1:8000/api/recruit/classroom/list'
        }
      ).then(function (response) {
        if (response.data.message === 'error') {
          this.$notify.error({
            title: '错误',
            message: '无法获得数据'
          })
        }
      })
    }
  }
</script>
<style>
</style>
