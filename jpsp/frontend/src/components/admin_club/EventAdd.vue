<template>
  <el-form :model="AchievementForm" ref="AchievementForm" label-width="100px">
    <el-form-item
      v-for="(achievement, index) in AchievementForm.achievements"
      :label="'成就' + index"
      :key="achievement.key"
      :prop="'achievement.' + index + '.value'"
    >
      <el-input v-model="achievement.value"></el-input>
      <el-button @click.prevent="removeAchievement(achievement)">删除</el-button>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="submitForm">提交</el-button>
      <el-button @click="addAchievement">新增成就</el-button>
      <el-button @click="resetForm('AchievementForm')">重置</el-button>
    </el-form-item>
  </el-form>
</template>
<script>
  import axios from 'axios'
  export default {
    data () {
      return {
        AchievementForm: {
          achievements: [
            {
              value: ''
            }
          ],
          email: ''
        },
        error: false
      }
    },
    methods: {
      submitForm () {
        axios({
          method: 'POST',
          url: '',
          data: JSON.stringify({
            ClubId: this.GetClubId,
            ClubName: this.GetClubName,
            Achievements: this.AchievementForm.achievements,
            // TODO: Notice Array transfer to String
            Email: this.AchievementForm.email,
            Token: this.GetToken
          })
        }).then(function (response) {
          if (response.data.message === 'success') {
            console.log('success')
          }
          if (response.data.message === 'error') {
            console.log('error')
          }
        }.bind(this)).catch(function () {
          console.log('error')
        })
      },
      resetForm (formName) {
        this.$refs[formName].resetFields()
      },

      removeAchievement (item) {
        var index = this.AchievementForm.achievements.indexOf(item)
        if (index !== -1) {
          this.AchievementForm.achievements.splice(index, 1)
        }
      },
      addAchievement () {
        this.AchievementForm.achievements.push({
          value: '',
          key: Date.now()
        })
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
      },
      Authenticate () {
        return this.$store.state.Authenticated
      }
    }
  }
</script>
<style>
</style>
