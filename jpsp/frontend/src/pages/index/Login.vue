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
			<form>
					<input type="text" value="Username" v-model="LoginForm.UserName">
						<div class="key">
					<input type="password" value="Password" v-model="LoginForm.Password">
						</div>
			</form>
	<div class="signin">
		<input type="submit" value="登录" >
	</div>
</div>
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
        }
      }
    },
    methods: {
      onSubmit () {
        console.log('submit!')
        axios({
          method: 'POST',
          url: '../api/login/',
          data: {
            UserName: this.LoginForm.UserName,
            Password: this.LoginForm.Password,
            error: false
          }
        })
          .then(function (response) {
            if (response.data.message === 'User Authenticated') {
              console.log('success!!!')
              this.store.commit('Authenticate')
              this.store.commit('ApplyUserName', this.UserName)
            } else if (response.data.message === 'User Not Authenticated') {
              console.log('success!')
              this.error = true
            }
          })
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
