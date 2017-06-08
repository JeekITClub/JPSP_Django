<template>
  <el-table :data="RecruitClassroomList" border style="width: 100%">
    <el-table-column type="expand">
      <template scope="props">
        <el-button @click="ArrangeClassroom()"></el-button>
        <el-button @clcck="ArrangeClassroom()"></el-button>
        <el-button @click="ArrangeClassroom()"></el-button>
        <el-button @click="ArrangeClassroom()"></el-button>
        <el-button @click="ArrangeClassroom()"></el-button>
        <el-button @click="ArrangeClassroom()"></el-button>
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
        <span style="margin-left: 5px">{{ props.row.Date1 }} -- {{ props.row.Date2 }}</span>
      </el-table-column>
      <el-table-column label="结束时间">
        <span style="margin-left: 5px">{{ props.row.Date1 }} -- {{ props.row.Date3 }}</span>
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
        RecruitClassroom: [
          {
            Id: '',
            ClubName: '',
            Linkman: '',
            Date1: '',
            Date2: '',
            Date3: ''
          }
        ]
      }
    },
    methods: {
      ArrangeClassroom (classroom) {
        axios({
          method: 'POST',
          url: 'api/cd/',
          data: JSON.stringify({
            ClubName: '',
            Classroom: '',
            Date1: '',
            Date2: '',
            Date3: '',
            Token: ''
          })
        })
      },
      HandleDeleteSubmit (index) {
        // TODO: Problems here!
        axios({
          method: 'POST',
          url: 'api/cd/',
          data: JSON.stringify({
            RecruitClassroomID: '',
            Classroom: '',
            Token: ''
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
    }
  }
</script>
<style>
</style>
