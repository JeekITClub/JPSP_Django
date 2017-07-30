<template>
  <div class="container">
    <div class="row">
      <div class="col-md-12 col-lg-12">
        <h2>
          {{ Club.ClubName }}
        </h2>
      </div>
    </div>
    <div class="row">
      <el-carousel :interval="5000" arrow="" class="carousel">
        <el-carousel-item>
          <img src="../../assets/1.jpg">
        </el-carousel-item>
        <el-carousel-item>
          <img src="../../assets/2.jpg">
        </el-carousel-item>
      </el-carousel>
    </div>
    <div class="row">
      <div class="col-md-10 col-xs-15 col-sm-10 col-lg-10 Introduction">
        <p>{{ Club.Introduction }}</p>
      </div>
      <div class="col-md-2 col-xs-3 col-sm-2 col-lg-2 Join">
        <figure></figure>
        <button type="button" class="primary">加入该社团</button>
      </div>
    </div>
  </div>
</template>
<script>
  import axios from 'axios'
  export default {
    data () {
      return {
        ClubId: this.$route.params.ClubId,
        Club: {
          ClubName: 'Jeek',
          Introduction: 'DaAsASAS'
        },
        ImgItems: ['../../assets/1.jpg', '../../assets/2.jpg', '../../assets/3.jpg', '../../assets/4.jpg']
      }
    },
    computed: {
      Authenticate () {
        return this.$store.state.Authenticated
      },
      GetUserName () {
        return this.$store.state.UserName
      },
      GetToken () {
        return this.$store.state.Token
      }
    },
    mounted: function () {
      axios({
        method: 'POST',
        url: 'http://127.0.0.1:8000/api/clubprofile/get',
        data: JSON.stringify({
          Token: this.GetToken,
          ClubId: this.ClubId
        })
      }).then(function (response) {
        if (response.data.message === 'success') {
          this.Club = JSON.parse(response.data.data)
          console.log('success')
        } else {
          console.log('error')
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
