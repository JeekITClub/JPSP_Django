<!---component nav-top-->
<template>
<div>
<nav class="fh5co-nav" role="navigation">
    <div class="top-menu">
      <div class="container-fluid">
        <div class="row">
          <div class="col-xs-4">
            <div id="fh5co-logo"><a href="index.html">建平中学学生平台</a></div>
          </div>
          <div class="col-xs-8 text-right menu-1">
            <ul>
              <li class="active"><a href="index.html">首页</a></li>
              <li><a href="product.html">社团动态</a></li>
              <li class="has-dropdown"><a href="blog.html">社团介绍</a></li>
              <li><a href="about.html">关于</a></li>
              <li class="btn-cta"><a href="#"><span>登录</span></a></li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </nav>
</div>
</template>
<script>
  export default {
    data () {
      return {
        activeIndex: '1',
        activeIndex2: '1'
      }
    },
    methods: {
      handleSelect (key, keyPath) {
        console.log(key, keyPath)
      }
    }
  }
</script>
<style scoped>
  @import '../../assets/index/css/animate.css';
  @import '../../assets/index/css/icomoon.css';
  @import '../../assets/index/css/bootstrap.css';
  @import '../../assets/index/css/magnific-popup.css';
  @import '../../assets/index/css/flexslider.css';
  @import '../../assets/index/css/style.css';
</style>
