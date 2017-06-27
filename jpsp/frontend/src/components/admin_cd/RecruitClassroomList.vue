<template>
  <el-table :data="RecruitClassroomList" border style="width: 100%">
    <el-table-column type="expand">
      <template scope="props">
        <el-button @click="ArrangeClassroom('1',props.row.ClubName)"></el-button>
        <el-button @clcck="ArrangeClassroom('2',props.row.ClubName)"></el-button>
        <el-button @click="ArrangeClassroom('3',props.row.ClubName)"></el-button>
        <el-button @click="ArrangeClassroom('4',props.row.ClubName)"></el-button>
        <el-button @click="ArrangeClassroom('5',props.row.ClubName)"></el-button>
        <el-button @click="ArrangeClassroom('6',props.row.ClubName)"></el-button>
      </template>
    </el-table-column>
    <template scope="props">
      <el-table-column label="社团名称">
        <span style="margin-left: 10px">{{ props.row.Clubname }}</span>
      </el-table-column>
      <el-table-column label="联系人">
        <span style="margin-left: 10px">{{ props.row.Linkman }}</span>
      </el-table-column>
      <el-table-column label="开始时间">
        <span style="margin-left: 5px">{{ props.row.Date1 }}</span>
      </el-table-column>
      <el-table-column label="结束时间">
        <span style="margin-left: 5px">{{ props.row.Date2 }}</span>
      </el-table-column>
    </template>
    <el-table-column laebl="操作">
      <!--TODO: The function HandleDeleteSubmit needs to be rewriten. !-->
      <el-button size="small" type="danger" @click="HandleDeleteSubmit(scope.$index)">
        删除
      </el-button>
    </el-table-column>
  </el-table>
</template>
<script>
  import axios from 'axios'
  export default {
    data () {
      return {
        RecruitClassroom: []
      }
    },
    methods: {
      ArrangeClassroom (classroom, clubname, date1, date2, date3) {
        axios({
          method: 'POST',
          url: 'http://127.0.0.1/api/cd/classroom/arrange/submit',
          data: JSON.stringify({
            ClubName: clubname,
            Classroom: classroom,
            Date1: date1,
            Date2: date2,
            Date3: date3,
            Token: this.GetToken
          })
        })
      },
      HandleDeleteSubmit (index) {
        // TODO: Problems here!
        axios({
          method: 'POST',
          url: 'http://127.0.0.1/api/cd/classroom/deny/submit',
          data: JSON.stringify({
            RecruitClassroomID: '',
            Classroom: '',
            Token: this.GetToken
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
        url: 'http://127.0.0.1:8000/api/cd/classroom/get',
        data: JSON.stringify({
          Token: this.GetToken
        })
      }).then(function (response) {
        if (response.data.message === 'success') {
          this.RecruitClassroomTable = JSON.parse(response.data.data)
          console.log('success')
        } else {
          console.log('error')
        }
      }.bind(this))
    }
  }
</script>
<style>
</style>
