<template>
  <el-row v-if="GetIndexAuthenticated===true">
    <el-col :span="4">
      <el-menu mode="vertical" class="el-menu-vertical-demo" :default-active=activeIndex @select="handleSelect">
        <el-menu-item-group title="个人中心">
          <el-menu-item index="1">用户信息</el-menu-item>
          <el-menu-item index="2">更改密码</el-menu-item>
        </el-menu-item-group>
        <el-menu-item-group title="活动">
          <el-menu-item index="3">已加入活动</el-menu-item>
          <el-menu-item index="4">参加过的活动</el-menu-item>
        </el-menu-item-group>
        <el-menu-item-group title="社团">
          <el-menu-item index="5">已加入社团</el-menu-item>
        </el-menu-item-group>
      </el-menu>
    </el-col>
    <el-col :span="20">
      <!-- 用户信息 -->
      <div v-if="activeIndex==='1'">
        <el-col :span="8" :offset="2">
          <el-form ref="ProfileForm" :model="ProfileForm">
            <el-form-item prop="UserName" label="用户名" :required="true">
              <el-input v-model="ProfileForm.UserName"></el-input>
            </el-form-item>
            <el-form-item prop="Grade" label="年级" :required="true">
              <el-select v-model="ProfileForm.Grade" value="">
                <el-option label="高一" value="1"></el-option>
                <el-option label="高二" value="2"></el-option>
                <el-option label="高三" value="3"></el-option>
              </el-select>
            </el-form-item>
            <el-form-item prop="Class" label="班级" :required="true">
              <el-select v-model="ProfileForm.Class" value="">
                <el-option label="1" value="1"></el-option>
                <el-option label="2" value="2"></el-option>
                <el-option label="3" value="3"></el-option>
                <el-option label="4" value="4"></el-option>
                <el-option label="5" value="5"></el-option>
                <el-option label="6" value="6"></el-option>
                <el-option label="7" value="7"></el-option>
                <el-option label="8" value="8"></el-option>
                <el-option label="9" value="9"></el-option>
                <el-option label="10" value="10"></el-option>
                <el-option label="11" value="11"></el-option>
                <el-option label="12" value="12"></el-option>
                <el-option label="13" value="13"></el-option>
              </el-select>
            </el-form-item>
            <el-form-item prop="AttendYear" label="入学年份" :required="true">
              <el-input v-model="ProfileForm.AttendYear"></el-input>
            </el-form-item>
            <el-form-item label="QQ" prop="QQ">
              <el-input v-model="ProfileForm.QQ"></el-input>
            </el-form-item>
            <el-form-item label="电子邮箱" prop="Email">
              <el-input v-model="ProfileForm.Email"></el-input>
            </el-form-item>
            <el-form-item label="手机号码" prop="Phone">
              <el-input v-model="ProfileForm.Phone"></el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="onSubmit()">更改</el-button>
              <el-button>取消</el-button>
            </el-form-item>
          </el-form>
        </el-col>
      </div>

      <!-- 更改密码 -->
      <div v-else-if="activeIndex==='2'">
        <h1 class="select-title">不准改</h1>
      </div>

      <!-- 已加入活动 -->
      <div v-else-if="activeIndex==='3'">
        <h1 class="select-title">已加入活动</h1>
      </div>

      <!-- 参加过的活动 -->
      <div v-else-if="activeIndex==='4'">
        <h1 class="select-title">参加过的活动</h1>
      </div>

      <!-- 已加入社团 -->
      <div v-else-if="activeIndex==='5'">
        <h1 class="select-title">已加入社团</h1>
        <div class="container">
          <div class="col-sm-6 col-md-4" v-for="club in ProfileForm.Club" :key="club">
            <div class="thumbnail">
              <div class="caption">
                <h3 class="name">{{ club }}</h3>
                <button class="btn btn-danger" type="button" @click="quitClub(club.id)">我要退出</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </el-col>
  </el-row>
  <el-row v-else>
    <h1 style="text-align: center">您还未登录，请返回登录！</h1>
  </el-row>
</template>
<script>
  import { getCookie } from 'tiny-cookie'
  import axios from 'axios'
  export default {
    data () {
      return {
        ProfileForm: {
          UserName: '',
          Grade: '',
          Class: '',
          QQ: '',
          Email: '',
          Phone: '',
          Club: [],
          AttendYear: ''
//          Activity: [
//            [],
//            []
//          ]
        },
        activeIndex: '1'
      }
    },
    computed: {
      GetUserId () {
        return getCookie('UserId')
      },
      GetIndexToken () {
        return getCookie('IndexToken')
      },
      GetIndexAuthenticated () {
        return getCookie('IndexAuthenticated')
      },
      GetUserName () {
        return getCookie('UserName')
      },
      /**
       * @return {string}
       */
      GetApi () {
        return this.$store.state.Api
      }
    },
    methods: {
      onSubmit () {
        axios({
          method: 'POST',
          url: this.GetApi + 'user/profile/submit',
          data: JSON.stringify({
            'UserId': this.GetUserId,
            'Token': this.GetIndexToken,
            'UserName': this.ProfileForm.UserName,
            'Grade': this.ProfileForm.Grade,
            'Class': this.ProfileForm.Class,
            'QQ': this.ProfileForm.QQ,
            'Email': this.ProfileForm.Email,
            'Phone': this.ProfileForm.Phone,
            'Club': this.ProfileForm.Club
          })
        }).then(function (response) {
          if (response.data.message === 'success') {
            this.ProfileForm = JSON.parse(response.data.data)
          } else {
            this.$notify.error({
              title: '错误',
              message: '无法获得数据'
            })
          }
        }.bind(this))
      },
      handleSelect (key) {
        this.activeIndex = key
      },
      quitClub (ClubId) {
        // TODO: delete club from tuple(Club)
        axios({
          method: 'POST',
          url: this.GetApi + 'club/quit',
          data: JSON.stringify({
            UserId: this.GetUserId,
            IndexToken: this.GetIndexToken,
            ClubId: ClubId
          })
        })
          .then(function (response) {
            if (response.data.message === 'success') {
              this.$notify({
                'title': '成功',
                'message': '成功退出社团',
                'type': 'success'
              })
            } else {
              this.$notify.error({
                title: '错误',
                message: '无法获得数据'
              })
            }
          }.bind(this))
      }
    },
    mounted: function () {
      axios({
        method: 'POST',
        url: this.GetApi + 'user/profile/get',
        data: JSON.stringify({
          UserId: this.GetUserId,
          Token: this.GetIndexToken
        })
      })
        .then(function (response) {
          if (response.data.message === 'success') {
            this.ProfileForm = JSON.parse(response.data.data)
          } else {
            this.$notify.error({
              title: '错误',
              message: '无法获得数据'
            })
          }
        }.bind(this))
    }
  }
</script>
<style scoped>
  .select-title {
    padding-left: 20px;
  }
</style>
