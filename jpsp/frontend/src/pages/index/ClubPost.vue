<template>
<div>
</div>
</template>
<script>
  export default {
    data () {
      return {
        Post: {
          Title: ''
        }
      }
    },
    methods: {
      onSubmit () {
        console.log('submit!')
      }
    },
    computed: {
      Authenticate () {
        return this.$store.state.Authenticated
      },
      GetToken () {
        return this.$store.state.Token
      },
      GetUserName () {
        return this.$store.state.UserName
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
