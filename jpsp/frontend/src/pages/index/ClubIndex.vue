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
      <el-carousel :interval="5000" arrow="never">
        <el-carousel-item v-for="item in 4" :key="item">
          <h3>{{ item }}</h3>
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
          Introduction: 'DaAsASASDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD'
        }
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
  .el-carousel__item h3 {
    color: #475669;
    font-size: 18px;
    opacity: 0.75;
    line-height: 300px;
    margin: 0;
  }

  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }

  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }

  .Introduction {
    margin-top: 3%;
    margin-button: 3%
  }

  .Join {
    margin-top: 3%;
    margin-button: 3%;
  }
</style>
