<template>
  <div>
    <!-- 这绝对不是彩蛋 -->
    <div v-if="ClubId === '303'" class="draw">
      <canvas></canvas>
    </div>
    <div v-else>
      <div class="hero is-primary">
        <div class="hero-body">
          <div class="container">
            <div class="colmuns">
              <div class="column">
                <p class="title">{{ Club.ClubName }}</p>
                <p class="subtitle">{{ Club.BriefIntro }}</p>
                <div class="content">
                  <p>社团QQ群: {{ Club.EnrollGroupQq }}</p>
                  <p>社团邮箱: {{ Club.Email }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="hero-foot">
          <div class="container">
            <nav class="tabs is-boxed">
              <ul>
                <li>
                  <a href="/">活动</a>
                </li>
                <li>
                  <a href="">杰出成员</a>
                </li>
              </ul>
            </nav>
          </div>
        </div>
      </div>
      <div class="section">
        <div class="container">
          <div class="columns">
            <div class="column is-three-quarters">
              <section class="section">
                <div class="container">
                  <h1 class="title">社团介绍</h1>
                  <div class="content">
                    <p>{{ Club.Introduction }}</p>
                  </div>
                </div>
              </section>
              <section class="section">
                <div class="container">
                  <h1 class="title">社团成就</h1>
                  <div class="content">
                    <p>{{ Club.Achievements }}</p>
                  </div>
                </div>
              </section>
            </div>
            <div class="column">
              <section class="section">
                <a class="button is-danger is-large" v-if="GetIndexAuthenticated === 'true'">未登陆</a>
                <a class="button is-warning is-large" v-else-if="Club.IfRecruit !== 'True'">社团未招新</a>
                <a class="button is-info is-large" @click="AttendClub" v-else>加入该社团</a>
              </section>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
  import axios from 'axios'

  export default {
    data () {
      return {
        ImgItems: ['../../assets/1.jpg', '../../assets/2.jpg', '../../assets/3.jpg', '../../assets/4.jpg'],
        ClubId: this.$route.params.ClubId,
        Club: {
          BriefIntro: '牛逼',
          Introduction: 'hellohellohellohellohellohellllohellohellohellohellohellohellohellohellohellohello',
          ClubName: 'Jeek信息社',
          Achievements: '开发JPSP!',
          IfRecruit: 'True'
        }
      }
    },
    methods: {
      AttendClub () {
        if (this.GetIndexAuthenticated !== 'true') {
          this.$router.push('/login')
        } else if (this.GetIndexAuthenticated === 'true') {
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
      GetUserId () {
        return this.$cookie.get('UserId')
      },
      GetIndexToken () {
        return this.$cookie.get('IndexToken')
      },
      GetUserName () {
        return this.$cookie.get('UserName')
      },
      GetIndexAuthenticated () {
        return this.$cookie.get('IndexAuthenticated')
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

  .draw {
    height: 900px;
  }
</style>
