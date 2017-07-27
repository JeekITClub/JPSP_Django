<template>
  <el-form :model="EventForm" ref="EventForm">
    <el-form-item>
      <el-input v-model="EventForm.Name" placeholder="事件名称"></el-input>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="submitForm">提交</el-button>
    </el-form-item>
  </el-form>
</template>
<script>
  import {getCookie} from 'tiny-cookie'
  import axios from 'axios'
  export default {
    data () {
      return {
        EventForm: {
          Name: ''
        }
      }
    },
    methods: {
      submitForm () {
        axios({
          method: 'POST',
          url: this.GetAPI + '/event/add',
          data: JSON.stringify({
            ClubId: this.GetClubId,
            Token: this.GetToken
          })
        }).then(function (response) {
          if (response.data.message === 'success') {
            console.log('success')
          }
          if (response.data.message === 'error') {
            console.log('error')
          }
        })
      }
    },
    computed: {
      GetClubId () {
        return getCookie('ClubId')
      },
      GetToken () {
        return getCookie('ClubToken')
      },
      GetAPI () {
        return this.$store.state.API
      }
    }
  }
</script>
<style>
</style>
