<template>
  <div>
    <el-table :data="Members" stripe>
      <el-table-column prop="MemberName" label="社员姓名" width="">
      </el-table-column>
      <el-table-column prop="MemberGrade" label="社员年级" width="">
      </el-table-column>
      <el-table-column prop="MemberClass" label="社员班级" width="">
      </el-table-column>
      <el-table-column>
        <template>
          <el-button @click="" type="primary"></el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>
<script>
  import { getCookie } from 'tiny-cookie'
  export default {
    data () {
      return {
        Members: []
      }
    },
    methods: {
      addMember () {
        console.log('success')
      },
      deleteMember (member) {
        console.log('success')
      }
    },
    computed: {
      GetClubName () {
        return getCookie('ClubName')
      },
      GetClubId () {
        return getCookie('ClubId')
      },
      GetToken () {
        return getCookie('ClubToken')
      }
    }
  }
</script>
<style>
</style>
