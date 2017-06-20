<template>
<div class="main">
<h1>学生登录</h1>
<div class="login-form">
	<div class="close"> </div>
		<div class="head-info">
			<label class="lbl-1"> </label>
			<label class="lbl-2"> </label>
			<label class="lbl-3"> </label>
		</div>
			<div class="clear"> </div>
	<div class="avtar">
		<img src="../../assets/index/images/avtar.png" />
	</div>
		<el-form>
			<el-form-item label="学号">
				<el-input type="text" v-model="LoginForm.UserId"></el-input>
			</el-form-item>
			<el-form-item label="密码">
				<el-input type="password" v-model="LoginForm.Password"></el-input>
			</el-form-item>
			<el-button type="primary" @click="onSubmit">登陆</el-button>
		</el-form>
</div>
</div>
</template>

<script>
  import axios from 'axios'
  export default {
    data () {
      return {
        LoginForm: {
          UserId: '',
          Password: ''
        }
      }
    },
    methods: {
      onSubmit () {
        axios({
          method: 'POST',
          url: 'http://127.0.0.1/api/login',
          data: {
            UserId: this.LoginForm.UserId,
            Password: this.LoginForm.Password
          }
        })
          .then(function (response) {
            if (response.data.message === 'User Authenticated') {
              console.log('success!!!')
              this.$store.commit('Authenticated', true)
              this.$store.commit('ApplyUserName', response.data.UserName)
              this.$store.commit('ApplyToken', response.data.Token)
            } else if (response.data.message === 'User Not Authenticated') {
              console.log('Failed')
            }
          }.bind(this))
          .catch(function (error) {
            console.log(error)
          })
      }
    }
  }
</script>

<style scoped>
  @import '../../assets/index/css/bootstrap.css';
  @import '../../assets/index/css/login.css';

  .el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 150px;
    margin: 0;
  }

  .el-carousel__item:nth-child(2n) {
     background-color: #99a9bf;
  }

  .el-carousel__item:nth-child(2n+1) {
     background-color: #d3dce6;
  }
</style>
