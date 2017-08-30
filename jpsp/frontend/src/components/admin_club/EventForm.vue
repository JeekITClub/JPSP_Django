<template>
  <el-form :model="EventForm" ref="EventForm">
    <el-form-item>
      <el-input v-model="EventForm.Name" placeholder="事件名称"></el-input>
    </el-form-item>
    <el-form-item label="" class="EditorItem">
      <quill-editor v-model="EventForm.Content" ref="myQillEditor" class="Editor">
      </quill-editor>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="submitForm" size="large">提交</el-button>
    </el-form-item>
  </el-form>
</template>
<script>
  import axios from 'axios'
  export default {
    data () {
      return {
        EventForm: {
          Name: '',
          Content: ''
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
          }),
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
          }
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
        return this.$cookie.get('ClubId')
      },
      GetToken () {
        return this.$cookie.get('ClubToken')
      },
      GetAPI () {
        return this.$store.state.API
      }
    }
  }
</script>
<style scoped>
  .Editor {
    height: 550px;
    min-height: 500px;
    max-height: 600px;
  }
  .EditorItem {
    margin-bottom: 2%;
    height: 640px;
    min-height: 590px;
    max-height: 690px;
  }
</style>
