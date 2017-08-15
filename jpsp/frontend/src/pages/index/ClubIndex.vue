<template>
  <div>
    <!-- 这绝对不是彩蛋 -->
    <div v-if="ClubId === '303'" class="draw">
      <canvas></canvas>
    </div>
    <div v-else>
      <div class="club-head">
        <div class="container">
          <!--<div class="row">-->
          <!--<el-carousel :interval="5000" arrow="" class="carousel">-->
          <!--<el-carousel-item v-for="item in ImgItems" :key="item">-->
          <!--<img :src="item">-->
          <!--</el-carousel-item>-->
          <!--</el-carousel>-->
          <!--</div>-->
          <div>
            <div class="club-logo col-md-4">
              <img src="../../assets/dp.jpg">
            </div>
            <div class="club-info col-md-8">
              <p class="club-name">{{ Club.ClubName }}</p>
              <ul>
                <li>社团QQ群: {{ Club.EnrollGroupQq }}</li>
                <li>社团邮箱: {{ Club.Email }}</li>
                <li>社团标签: {{ Club.Label }}</li>
              </ul>
              <div class="col-md-2 col-xs-3 col-sm-2 col-lg-2 Join">
                <!-- TODO: 验证是否已加入 -->
                <button class="btn btn-primary" type="button" @click="AttendClub" v-if="1===1">加入该社团</button>
                <p v-else>已加入该社团</p>
              </div>
            </div>
          </div>

        </div>
      </div>
      <div class="container club-detail">
        <div>
          <h3>社团介绍</h3>
          <p>{{ Club.Introduction }}</p>
        </div>
        <div>
          <h3>社团成就</h3>
          <p>{{ Club.Achievements }}</p>
        </div>
      </div>
      <!--<div class="col-md-10 col-xs-15 col-sm-10 col-lg-10 Introduction">-->
      <!--<p>{{ Club.Introduction }}</p>-->
      <!--</div>-->
    </div>
  </div>
</template>
<script>
  import axios from 'axios'
  import {getCookie} from 'tiny-cookie'

  export default {
    data () {
      return {
        ImgItems: ['../../assets/1.jpg', '../../assets/2.jpg', '../../assets/3.jpg', '../../assets/4.jpg'],
        ClubId: this.$route.params.ClubId,
        Club: {
          Introduction: 'hellohellohellohellohellohellllohellohellohellohellohellohellohellohellohellohello',
          ClubName: 'Jeek信息社',
          Achievements: '开发JPSP!'
        }
      }
    },
    methods: {
      AttendClub () {
        if (this.Authenticated !== true) {
          this.$router.push('/login')
        } else if (this.Authenticated === true) {
          axios({
            method: 'POST',
            url: this.GetApi + 'club/attend',
            data: JSON.stringify({
              ClubId: this.ClubId,
              UserId: this.GetUserId,
              IndexToken: this.GetIndexToken
            })
          })
            .then(function (response) {
              if (response.data.message === 'success') {
                this.$notify({
                  'type': 'success',
                  'message': '成功加入！请等待社长审核!',
                  'title': '成功!'
                })
              } else {
                this.$notify.error({
                  'message': '错误',
                  'title': '错误'
                })
              }
            })
        }
      }
    },
    computed: {
      GetIndexAuthenticated () {
        return getCookie('IndexAuthenticated')
      },
      GetUserName () {
        return getCookie('UserName')
      },
      GetIndexToken () {
        return getCookie('IndexToken')
      },
      GetUserId () {
        return getCookie('UserId')
      },
      /**
       * @return {string}
       */
      GetApi () {
        return this.$store.state.Api
      }
    },
    mounted: function () {
      axios({
        method: 'POST',
        url: this.GetApi + 'club/profile/get',
        data: JSON.stringify({
          ClubId: this.ClubId
        })
      }).then(function (response) {
        if (response.data.message === 'success') {
          this.Club = JSON.parse(response.data.data)
        } else {
        }
      }.bind(this))
    },
    created () {
      if (this.ClubId === '303') {
        this.BackGround()
      }
    }
  }
</script>
<style scoped>
  .club-head {
    padding-top: 50px;
    padding-left: 10%;
    padding-right: 10%;
    padding-bottom: 1%;
    border-bottom: 1px solid #eee;
    background-color: #fafbfc;
  }

  .club-name {
    font-size: 2em;
  }

  .club-info {
    padding-left: 5%;
  }

  .club-logo {
    width: 200px;
    height: 200px;
  }

  .club-logo img {
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    margin: auto;
    max-width: 100%;
    max-height: 100%;
  }

  .club-detail {
    padding-top: 4%;
    padding-left: 10%;
    padding-right: 10%;
  }

  .Introduction {
    margin-top: 3%;
    margin-bottom: 3%;
  }

  .Join {
    margin-top: 3%;
    margin-bottom: 3%;
  }

  .carousel {
    width: 100%;
    height: 100%;
  }

  .draw {
    height: 900px;
  }
</style>
