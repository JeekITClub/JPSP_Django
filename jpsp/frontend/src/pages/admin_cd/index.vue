<template>
  <el-row>
    <el-col :span="24">
      <div class="grid-content bg-purple-dark">
        <el-menu theme="dark" :default-active="activeIndex" class="el-menu-demo" mode="horizontal"
                 @select="handleSelect">
          <el-menu-item index="1" disabled="" route="">处理中心</el-menu-item>
          <el-submenu index="2">
            <template slot="title">我的工作台</template>
            <el-menu-item index="2-1" disabled="" route="">选项1</el-menu-item>
            <el-menu-item index="2-2" disabled="" route="">选项2</el-menu-item>
            <el-menu-item index="2-3" disabled="" route="">选项3</el-menu-item>
          </el-submenu>
          <el-menu-item index="3" disabled="" route=""><a href="https://www.ele.me" target="_blank">订单管理</a>
          </el-menu-item>
        </el-menu>
      </div>
    </el-col>
  </el-row>
  <div class="LoginForm">
      <el-row class="tac">
        <el-col :span="8" :offset="8">
          <el-form ref="LoginForm" :model="LoginForm" v-if="Authenticate===false">
            <el-form-item label="学号" :required=true>
              <el-input v-model="LoginForm.UserName" placeholder="学号" autofocus=""></el-input>
            </el-form-item>
            <el-form-item label="密码" :required=true>
              <el-input type="password" v-model="LoginForm.Password" placeholder="密码">
              </el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="onSubmit">登陆</el-button>
            </el-form-item>
            <el-form-item>
              <p v-if="settings.NotAuthenticated===true">登陆失败</p>
            </el-form-item>
          </el-form>
          <h1 v-if="Authenticate===true">已登录</h1>
        </el-col>
      </el-row>
    </div>
</template>
<script>
  import axios from 'axios'
  export default {
    data () {
      return {
        LoginForm: {
          UserName: '',
          Password: ''
        },
        settings: {
          NotAuthenticated: false
        }
      }
    },
    methods: {
      onSubmit () {
        axios({
          method: 'POST',
          url: '',
          data: JSON.stringify({
            UserName: this.LoginForm.UserName,
            Password: this.LoginForm.Password
          })
        }).then(function (response) {
            if (response.data.message === 'User Authenticated') {
              this.$store.commit('Authenticate')
              this.$store.commit('ApplyUserName', this.UserName)
            } else if (response.data.message === 'User Not Authenticated') {
              this.data.settings.NotAuthenticated = true
            }
          })
          .catch(function (error) {
            console.log(error)
          })
      }
    },
    computed: {
      Authenticate () {
        return this.$store.state.Authenticated
      }
    }
  }
</script>
<style>
  .el-row {
    margin-bottom: 20px;

  }
  .bg-purple-dark {
    background: #99a9bf;
  }

  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }

</style>
