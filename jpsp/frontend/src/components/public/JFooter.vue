<!---component jfooter-->
<template>
      <footer id="fh5co-footer" role="contentinfo">
    <div class="container">
      <div class="row row-pb-md">
        <div class="col-md-4 fh5co-widget">
          <h4>Ink's</h4>
          <p>Facilis ipsum reprehenderit nemo molestias. Aut cum mollitia reprehenderit. Eos cumque dicta adipisci architecto culpa amet.</p>
        </div>
        <div class="col-md-4 col-md-push-1">
          <h4>Links</h4>
          <ul class="fh5co-footer-links">
            <li><a href="#">Home</a></li>
            <li><a href="#">Practice Areas</a></li>
            <li><a href="#">Won Cases</a></li>
            <li><a href="#">Blog</a></li>
            <li><a href="#">About us</a></li>
          </ul>
        </div>

        <div class="col-md-4 col-md-push-1">
          <h4>Contact Information</h4>
          <ul class="fh5co-footer-links">
            <li>地址：浦东崮山路517号、385号(北校区)<br>电话：021-58851542</li>
            <li>传真：021-38821698</li>
            <li><a href="tel://1234567920">邮箱：jpzxxzyx2016@163.com</a></li>
            <li><a href="mailto:info@yoursite.com">版权所有：Jeek</a></li>
          </ul>
        </div>

      </div>

      <div class="row copyright">
        <div class="col-md-12 text-center">
          <p>
            <ul class="fh5co-social-icons">
              <li><a href="#"><i class="icon-twitter"></i></a></li>
              <li><a href="#"><i class="icon-facebook"></i></a></li>
              <li><a href="#"><i class="icon-linkedin"></i></a></li>
              <li><a href="#"><i class="icon-dribbble"></i></a></li>
            </ul>
          </p>
        </div>
      </div>

    </div>
  </footer>
</template>
<script>
  export default {
    data () {
      return {}
    },
    methods: {
      handleSelect (key, keyPath) {
        console.log(key, keyPath)
      }
    }
  }
</script>
<style>
  @import '../../assets/index/css/animate.css';
  @import '../../assets/index/css/icomoon.css';
  @import '../../assets/index/css/bootstrap.css';
  @import '../../assets/index/css/magnific-popup.css';
  @import '../../assets/index/css/flexslider.css';
  @import '../../assets/index/css/style.css';

  .footer {
    position: relative;
    bottom: 0;
    width: 100%;
    height: 6%;
    background-color: #f5f5f5;
  }
  .footer .container {
    padding-top: 10px;
  }
</style>
