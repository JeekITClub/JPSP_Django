<template>
  <div>
    <div class="tile is-ancestor">
      <div class="tile is-vertical is-8">
        <div class="tile">
          <div class="tile is-parent is-vertical">
            <article class="tile is-child notification is-primary">
              <p class="title">评分最高社团</p>
              <div class="content best-club"><p>{{ best_club }}</p></div>
            </article>
            <article class="tile is-child notification is-danger">
              <p class="title">评分最差社团</p>
              <div class="content worst-club"><p>{{ worst_club }}</p></div>
            </article>
          </div>
          <div class="tile is-parent">
            <article class="tile is-child notification is-info">
              <p class="title">剩余未审核社团活动记录</p>
              <div class="content post-number"><p>{{ unconfirmed_post_number }}</p></div>
            </article>
          </div>
        </div>
        <div class="tile">
          <div class="tile is-parent is-vertical">
            <article class="tile is-child notification is-success">
              <p class="title">最新进行活动</p>
              <p class="subtitle">by {{ activity_club }}</p>
              <div class="content"><p>{{ activity }}</p></div>
            </article>
            <article class="tile is-child notification is-warning">
              <p class="title">最新上传文件</p>
              <p class="subtitle">by {{ upload_club}}</p>
              <div class="content"><p>{{ upload }}</p></div>
            </article>
          </div>
        </div>
      </div>
      <div class="tile is-parent is-vertical">
        <article class="tile is-child notification is-success">
          <div class="content">
            <p class="title">最新公告</p>
            <div class="content">
              <p>{{ message }}</p>
            </div>
          </div>
        </article>
        <article class="tile is-child notification">
          <div class="field">
            <label class="label">发布公告</label>
            <div class="control">
              <textarea class="textarea" placeholder="e.g. 所有社长明天于x点到圆厅开会！" v-model="message"
                        style="height: 200px;"></textarea>
            </div>
          </div>
          <div class="field is-grouped">
            <div class="control">
              <button class="button is-primary" @click="submitMessage">Submit</button>
            </div>
          </div>
        </article>
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
        best_club: 'Jeek信息社',
        worst_club: 'xxx',
        unconfirmed_post_number: '0',
        activity_club: 'Jeek信息社',
        activity: '开发建平中学学生平台',
        upload_club: 'Jeek信息社',
        upload: '开发建平中学学生平台',
        message: ''
      }
    },
    mounted: function () {
      axios({
        method: 'GET',
        url: this.GetApi + '/message'
      })
        .then(function (response) {
          if (response.data.message === 'success') {
            this.message = JSON.parse(response.data.data)
          }
          // TODO: err handler
        })
    },
    methods: {
      submitMessage () {
        axios({
          method: 'POST',
          url: this.GetApi + '/message',
          data: Qs.stringify({
            UserId: this.GetUserId,
            CDToken: this.GetCDToken,
            Message: this.message
          })
        })
          .then(function (response) {
            if (response.data.message === 'success') {
              this.$notify({
                'title': '成功',
                'message': '成功发布公告',
                'type': 'success'
              })
            } else {
              this.$notify.error({
                title: '错误',
                message: '发送公告失败'
              })
            }
          }.bind(this))
      }
    },
    computed: {
      GetUserId () {
        return this.$cookie.get('CDUserId')
      },
      GetCDToken () {
        return this.$cookie.get('CDToken')
      },
      GetUserName () {
        return this.$cookie.get('CDUserName')
      },
      GetCDAuthenticated () {
        return this.$cookie.get('CDAuthenticated')
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
  .post-number {
    font-size: 50px;
    text-align: center;
    margin-top: 25%;
  }

  .best-club {
    font-size: 50px;
    text-align: center;
  }

  .worst-club {
    font-size: 50px;
    text-align: center;
  }
</style>
