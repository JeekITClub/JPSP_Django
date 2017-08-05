<template>
   <div>
     <div>
       <p class="lead">社团活动记录列表</p>
     </div>
     <div align="right">
       <el-button @click="GoToPostForm" type="primary" size="big">添加社团记录</el-button>
     </div>
    <el-tabs v-model="TabsValue" type="card">
      <el-tab-pane label="未审核" name="UnStared">
        <club_post_list type="UnStared" user="CD"></club_post_list>
      </el-tab-pane>
      <el-tab-pane label="已审核" name="Stared">
        <club_post_list type="Stared" user="CD"></club_post_list>
      </el-tab-pane>
      <el-tab-pane label="未通过" name="UnPassed">
        <club_post_list type="UnPassed" user="CD"></club_post_list>
      </el-tab-pane>
      <el-tab-pane label="所有" name="All">
        <club_post_list type="All" user="CD"></club_post_list>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>
<script>
  import PostList from '../../components/public/PostList.vue'
  export default {
    components: {
      'club_post_list': PostList
    },
    data () {
      return {
        TabsValue: 'Stared'
      }
    },
    methods: {
      GoToPostForm () {
        this.$router.push('/post/form')
      }
    }
  }
</script>
<style>
</style>
