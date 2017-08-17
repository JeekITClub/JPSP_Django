<template>
<section class="hero is-info is-fullheight">
  <div class="hero-body">
    <div class="container">
      <h1 class="title">
        建平学生平台
      </h1>
      <h2 class="subtitle">
        Jianping Students' Platform
      </h2>
    </div>
  </div>
</section>
</template>
<script>
  import { getCookie } from 'tiny-cookie'
  export default {
    data () {
      return {}
    },
    methods: {},
    computed: {
      GetUserId () {
        return getCookie('UserId')
      },
      GetIndexToken () {
        return getCookie('IndexToken')
      },
      GetUserName () {
        return getCookie('UserName')
      },
      GetIndexAuthenticated () {
        return getCookie('IndexAuthenticated')
      },
      /**
       * @return {string}
       */
      GetApi () {
        return this.$store.state.Api
      }
    }
  }
</script>
<style scoped>
  @import '../../assets/index/css/animate.css';
  @import '../../assets/index/css/icomoon.css';
  @import '../../assets/index/css/magnific-popup.css';
  @import '../../assets/index/css/flexslider.css';
  @import '../../assets/index/css/style.css';

  .bi1 {
    background-image: url(../../assets/6.jpg);
  }

  .bi2 {
    background-image: url(../../assets/4.jpg);
  }

  .bi3 {
    background-image: url(../../assets/2.jpg);
  }

  .bi4 {
    background-image: url(../../assets/5.jpg);
  }

  .bi5 {
    background-image: url(../../assets/9.jpg);
  }

  .qsm {
    background-image: url(../../assets/Contributors/qsm.jpg);
  }

  .ncj {
    background-image: url(../../assets/Contributors/ncj.jpg);
  }

  .qlt {
    background-image: url(../../assets/Contributors/qlt.jpg);
  }

  .sms {
    background-image: url(../../assets/Contributors/sms.jpg);
  }
</style>
