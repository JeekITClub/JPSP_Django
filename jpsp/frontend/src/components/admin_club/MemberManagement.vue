<template>
  <el-table :data="members" stripe style="width: 100%">
    <el-table-column prop="MemberName" label="社员姓名" width="">
    </el-table-column>
    <el-table-column prop="MemberGrade" label="社员年级" width="">
    </el-table-column>
    <el-table-column prop="MemberClass" label="社员班级" width="">
    </el-table-column>
    <el-table-column>
      <el-button @click.prevent="deleteMember(Member)" type="primary"></el-button>
    </el-table-column>
  </el-table>
</template>
<script>
  export default {
    data () {
      return {
        members: [
          {
            Member: {
              Name: '',
              Grade: '',
              Class: ''
            }
          }
        ]
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
        return this.$store.state.UserName
      },
      GetClubId () {
        return this.$store.state.ClubId
      },
      GetToken () {
        return this.$store.state.Token
      }
    }
  }
</script>
<style>
</style>
