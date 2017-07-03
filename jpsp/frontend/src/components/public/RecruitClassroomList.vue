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
    <el-table-column v-if="user === 'CD' ">
      <template scope="scope">
        <el-button size="small" type="danger" @click="ClassroomConfirm('1', scope.row.pk)">
        </el-button>
        <el-button size="small" type="danger" @click="ClassroomConfirm('2', scope.row.pk)">
        </el-button>
        <el-button size="small" type="danger" @click="ClassroomConfirm('3', scope.row.pk)">
        </el-button>
        <el-button size="small" type="danger" @click="ClassroomConfirm('4', scope.row.pk)">
        </el-button>
        <el-button size="small" type="danger" @click="ClassroomConfirm('5', scope.row.pk)">
        </el-button>
        <el-button size="small" type="danger" @click="ClassroomConfirm('6', scope.row.pk)">
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
    prop: {
      user: {
        'default': 'Club'
      },
      type: {
        'default': 'Unconfirmed'
      }

    },
    methods: {
      ClassroomConfirm ( classroom, pk) {
        axios({
          method: 'POST',
          url: '',
          data: JSON.stringify({
            Id: pk,
            Classroom: classroom
          })
        })
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
          method: 'Post',}
        )}.then(function (response) {
      }.bind(this))
  },}
</script>
<style>
</style>
