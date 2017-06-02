<template>
<div>
</div>
</template>
<script>
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
              this.store.commit('LoginIn')
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
  @import url("//unpkg.com/element-ui@1.3.2/lib/theme-default/index.css");
  @import '../../assets/index/css/animate.css';
  @import '../../assets/index/css/icomoon.css';
  @import '../../assets/index/css/bootstrap.css';
  @import '../../assets/index/css/magnific-popup.css';
  @import '../../assets/index/css/flexslider.css';
  @import '../../assets/index/css/style.css';
  .img1{
    background-image: url(../../assets/index/images/img_bg_1.jpg);
  }

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
