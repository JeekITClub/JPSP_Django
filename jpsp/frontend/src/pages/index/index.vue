<template>
  <div>
    <div id="page">
      <aside id="fh5co-hero" class="js-fullheight">
        <div class="flexslider js-fullheight">
          <ul class="slides">
            <li class="bi1">
              <div class="overlay-gradient"></div>
              <div class="container-fluid">
                <div class="row">
                  <div class="col-md-6 col-md-offset-3 col-md-pull-3 js-fullheight slider-text slider-text-bg">
                    <div class="slider-text-inner">
                      <h1>我们回来了</h1>
                      <h2>还记得当年立下的flag吗？</h2>
                    </div>
                  </div>
                </div>
              </div>
            </li>
            <li class="bi5">
              <div class="overlay-gradient"></div>
              <div class="container-fluid">
                <div class="row">
                  <div class="col-md-6 col-md-offset-3 col-md-pull-3 js-fullheight slider-text slider-text-bg">
                    <div class="slider-text-inner">
                      <h1>互联网时代的社团</h1>
                      <h2>赶快体验一把</h2>
                      <p class="ct"><router-link to="Login">了解更多<i class="icon-arrow-right"></i></router-link></p>
                    </div>
                  </div>
                </div>
              </div>
            </li>
            <li class="bi3">
              <div class="overlay-gradient"></div>
              <div class="container-fluids">
                <div class="row">
                  <div class="col-md-6 col-md-offset-3 col-md-pull-3 js-fullheight slider-text slider-text-bg">
                    <div class="slider-text-inner">
                      <h1>想了解这个网站的怎么诞生的？</h1>
                      <h2>欢迎加入网站维护团队</h2>
                      <p class="ct"><router-link to="About">了解更多<i class="icon-arrow-right"></i></router-link></p>
                    </div>
                  </div>
                </div>
              </div>
            </li>
          </ul>
        </div>
      </aside>

      <div id="fh5co-content">
        <div class="video fh5co-video bi2">
        </div>
        <div class="choose">
          <div class="fh5co-heading">
            <h2>关于建平中学学生平台</h2>
            <p>全称Jianping Student's Platform </p>
          </div>
          <ul class="list-nav">
            <li><i class="icon-check2"></i>方便建平学生进行日常学校活动</li>
            <li><i class="icon-check2"></i>加强校内管理部门（如团委、学生会、自管会、社团部等）与学生的互动</li>
            <li><i class="icon-check2"></i>发布和获取实时资讯</li>
          </ul>
        </div>
      </div>

      <div id="fh5co-mission">
        <div class="container">
          <div class="row">
            <div class="col-md-6 col-md-offset-3 text-center">
              <h2>我们的使命</h2>
              <blockquote>
                <p>
                  打造校内互联网办公</p>
              </blockquote>
            </div>
          </div>
        </div>
      </div>
      <div id="fh5co-services">
        <div class="container">
          <div class="row">
            <div class="col-md-4 text-center">
              <div class="services">
            <span class="icon">
              <i class="icon-command"></i>
            </span>
                <div class="desc">
                  <h3><a href="#">幕后团队</a></h3>
                  <p>
                    建平中学学生平台最初由3名成员进行开发及维护
                  </p>
                </div>
              </div>
            </div>
            <div class="col-md-4 text-center">
              <div class="services">
            <span class="icon">
              <i class="icon-drop2"></i>
            </span>
                <div class="desc">
                  <h3><a href="#">网页设计 & UI</a></h3>
                  <p>
                    使用BootStrap + Element UI
                  </p>
                </div>
              </div>
            </div>
            <div class="col-md-4 text-center">
              <div class="services">
            <span class="icon">
              <i class="icon-anchor"></i>
            </span>
                <div class="desc">
                  <h3><a href="#">网页开发</a></h3>
                  <p>
                    建平中学学生平台采用Django + Vue.js 前后端分离架构</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div id="fh5co-about">
        <div class="container">
          <div class="row">
            <div class="col-md-8 col-md-offset-2 text-center fh5co-heading">
              <h2>Contributors</h2>
              <p>我们的征途是星辰大海</p>
            </div>
          </div>
          <div class="row">
            <div class="member">
              <div class="col-md-6 nopadding">
                <div class="author qsm"></div>
              </div>
              <div class="col-md-6 nopadding">
                <div class="desc">
                  <h3>邱世贸 Harvey Qiu</h3>
                  <span>2015届3班 JEEK信息社 副社长</span>
                  <p>JPSP前端、后端工程师、架构师<br>曾经的2018届金苹果电视台台长。放弃视频后改行编程。</p>
                  <br>
                  <blockquote>
                    <p>多读文档、多读源码就能变强。
                      <footer>邱世贸</footer>
                    </p>
                  </blockquote>
                </div>
              </div>
            </div>
            <div class="member">
              <div class="col-md-6 nopadding col-md-push-6">
                <div class="author ncj"></div>
              </div>
              <div class="col-md-6 nopadding col-md-pull-6">
                <div class="desc">
                  <h3>倪楚劼 Cheney Ni</h3>
                  <span>2015届13班 JEEK信息社 社长</span>
                  <p>
                    JPSP前端、后端工程师<br>编程爱好者，在担任班级电管员期间自学了C++，JAVA，安卓，python，Web开发，略懂算法和数据结构。</p>
                </div>
              </div>
            </div>
            <div class="member">
              <div class="col-md-6 nopadding">
                <div class="author qlt"></div>
              </div>
              <div class="col-md-6 nopadding">
                <div class="desc">
                  <h3>邱龙田 Artanic Qiu</h3>
                  <span>2015届3班</span>
                  <p>JPSP前端工程师</p>
                </div>
              </div>
            </div>
            <div class="member">
              <div class="col-md-6 no adding col-md-push-6">
                <div class="author sms"></div>
              </div>
              <div class="col-md-6 nopadding col-md-pull-6">
                <div class="desc">
                  <h3>苏孟帅 Monsell Su</h3>
                  <span>2015届11班 原JTV摄制组组长</span>
                  <p>
                    JPSP特邀摄影师<br>
                    热爱摄影，摄影技术高超，兼具轻微PS技能，是美化网站、居家必备的人才。</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div id="fh5co-started" class="bi4">
        <div class="overlay"></div>
        <div class="container">
          <div class="row">
            <div class="col-md-8 col-md-offset-2 text-center fh5co-heading">
              <h2>联系我们</h2>
              <p>
                JPSP是一个由三个高中生建立并维护的网站项目，但由于时间、资金有限，我们需要更多有志之士的帮助。如果你觉得这个网站还不错，并且有维护网站的兴趣和决心，请联系我们！<br>我们欢迎任何人的加入！<br><br>
              </p>
              <p><a href="https://github.com/AlienStudio" class="btn btn-default btn-lg">Contact Us</a></p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
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
