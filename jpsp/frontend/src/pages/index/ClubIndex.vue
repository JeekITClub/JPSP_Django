<template>
  <div>
    <!-- 这绝对不是彩蛋 -->
    <div>
      <div class="hero is-primary">
        <div class="hero-body">
          <div class="container">
            <div class="colmuns">
              <div class="column">
                <p class="title">{{ Club.ClubName }}</p>
                <div class="content">
                  <p>社团QQ群: {{ Club.QQGroup}}</p>
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
              <!--<section class="section">-->
              <!--<div class="container">-->
              <!--<h1 class="title">社团成就</h1>-->
              <!--<div class="content">-->
              <!--<p>{{ Club.Achievements }}</p>-->
              <!--</div>-->
              <!--</div>-->
              <!--</section>-->
            </div>
            <div class="column">
              <section class="section">
                <a class="button is-danger is-large" v-if="GetIndexAuthenticated !== 'true'">未登陆</a>
                <a class="button is-warning is-large" v-else-if="Club.IfRecruit !== 1">社团未招新</a>
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
  import Qs from 'qs'

  export default {
    data () {
      return {
        ClubId: this.$route.params.ClubId,
        Club: {
          Introduction: '',
          ClubName: '',
          IfRecruit: ''
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
            url: this.GetApi + 'clubships',
            data: Qs.stringify({
              ClubId: this.$route.params.ClubId,
              UserId: this.GetUserId,
              Token: this.GetIndexToken
            }),
            headers: {
              'Content-Type': 'application/x-www-form-urlencoded'
            }
          })
            .then(function (response) {
              if (response.data.message === 'success') {
                this.$notify.success({
                  'message': '成功加入！请等待社长审核!',
                  'title': '成功!'
                })
              } else {
                this.$notify.error({
                  'message': '无法加入社团',
                  'title': '错误'
                })
              }
            }.bind(this))
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
        method: 'GET',
        url: this.GetApi + 'clubs/profile',
        params: {
          ClubId: this.ClubId
        }
      }).then(function (response) {
        if (response.data.message === 'success') {
          this.Club = response.data.data
        } else {
          this.$notify.error({
            'message': '无法获得社团信息',
            'title': 'Error'
          })
        }
      }.bind(this))
    },
    created () {
      if (this.ClubId === '303') {
        console.log('hello')
      }
    }
  }
</script>
<style scoped>
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
</style>
