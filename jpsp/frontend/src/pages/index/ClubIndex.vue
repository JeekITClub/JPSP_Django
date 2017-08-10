<template>
  <div class="container">
    <div class="row">
      <div class="col-md-12 col-lg-12">
        <p class="lead">
          {{ Club.ClubName }}
        </p>
      </div>
    </div>
    <!--<div class="row">-->
      <!--<el-carousel :interval="5000" arrow="" class="carousel">-->
        <!--<el-carousel-item v-for="item in ImgItems" :key="item">-->
          <!--<img :src="item">-->
        <!--</el-carousel-item>-->
      <!--</el-carousel>-->
    <!--</div>-->
    <div class="row">
      <div class="col-md-10 col-xs-15 col-sm-10 col-lg-10 Introduction">
        <p>{{ Club.Introduction }}</p>
      </div>
      <div class="col-md-2 col-xs-3 col-sm-2 col-lg-2 Join">
        <button class="btn btn-primary" type="button" @click="AttendClub" v-if>加入该社团</button>

      </div>
    </div>
    <div class="row">
      <div class="col-md-10 col-xs-15 col-sm-10 col-lg-10">
        <p>{{ Club.Achievements }}</p>
      </div>
    </div>
  </div>
</template>
<script>
  import axios from 'axios'
  import { getCookie } from 'tiny-cookie'
  export default {
    data () {
      return {
        ImgItems: ['../../assets/1.jpg', '../../assets/2.jpg', '../../assets/3.jpg', '../../assets/4.jpg'],
        ClubId: this.$route.params.ClubId,
        Club: {
          Introduction: 'hello',
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
              UserName: this.GetUserName
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
      Authenticated () {
        return getCookie('IndexAuthenticated')
      },
      GetUserName () {
        return getCookie('UserName')
      },
//      GetToken () {
//        return this.$store.state.Token
//      },
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
    }
  }
</script>
<style scoped>
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
</style>
