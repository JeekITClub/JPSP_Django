<template>
  <div class="container text-center">
    <div>
      <p class="lead">
        建平中学学生平台（以下简称为JPSP）由建平中学学生社团Jeek信息社独立开发。
      </p>
      <p>
        JPSP采用<a href="https://www.djangoproject.com/" target="_blank">Django</a>
        +
        <a href="http://cn.vuejs.org/" target="_blank">Vue.js</a>
        +
        <a href="https://www.mysql.com/" target="_blank">MySQL</a>
        为主要技术栈,
        并使用了
        <a href="http://nginx.org/" target="_blank">Nginx</a>、
        <a href="https://github.com/unbit/uwsgi" target="_blank">uwsgi</a>、
        <a href="http://getbootstrap.com/" target="_blank">Bootstrap</a>、
        <a href="https://www.npmjs.com/package/axios" target="_blank">Axios</a>、
        <a href="http://element.eleme.io/" target="_blank">ElementUI</a>、
        <a href="https://www.daocloud.io/" target="_blank">DaoCloud</a>、
        <a href="http://webpack.github.io/" target="_blank">WebPack</a>、
        <a href="https://www.npmjs.com/" target="_blank">NPM</a>
        等各项技术
      </p>
      <p>特别感谢<a href="" target="_blank">Github</a>以及<a href="" target="_blank">JetBrains</a></p>
    </div>
    <div>
      <h1>Contributors</h1>
      <p><a href="https://github.com/nichujie">2018届（13）班倪楚劼</a>
        <span>、</span>
        <a href="https://alienmao.github.io/">2018届（3）班邱世贸</a>
        <!--<span>、</span>-->
        <!--<a href="https://github.com/Artanic30">2018届（3）班邱龙田</a>-->
      </p>
    </div>
    <div>
      <h1>
        后端
      </h1>
      <p>后端架构为Nginx+uwsgi+Django</p>
      <h1>
        前端
      </h1>
      <p>
        前端采用了Vue.js框架，使用axios进行与后端交互，使用Vuex进行状态管理。
      </p>
    </div>
  </div>
</template>
<script>
  export default {
    data () {
      return {}
    }
  }
</script>
<style>
</style>
