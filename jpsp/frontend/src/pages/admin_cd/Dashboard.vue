<template>
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
    <div class="tile is-parent">
      <article class="tile is-child notification is-success">
        <div class="content">
          <p class="title">最新公告</p>
          <div class="content">
            <p>该功能暂未开放</p>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
          </div>
        </div>
      </article>
    </div>
  </div>
</template>
<script>
  export default {
    data () {
      return {
        best_club: 'Jeek信息社',
        worst_club: 'xxx',
        unconfirmed_post_number: '0',
        activity_club: 'Jeek信息社',
        activity: '开发建平中学学生平台',
        upload_club: 'Jeek信息社',
        upload: '开发建平中学学生平台'
      }
    }
  }
</script>
<style scoped>
  .post-number {
    font-size:50px;
    text-align: center;
    margin-top: 25%;
  }
  .best-club {
    font-size:50px;
    text-align: center;
  }
  .worst-club {
    font-size:50px;
    text-align: center;
  }
</style>
