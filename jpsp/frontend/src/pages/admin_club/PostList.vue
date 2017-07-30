<template>
   <div>
     <div align="right">
       <el-button @click="GoToPostForm()" type="primary" size="big">添加社团记录</el-button>
     </div>
    <el-tabs v-model="TabsValue" type="card">
      <el-tab-pane label="未审核" name="UnStared">
        <club_postlist type="UnStared" user="CD"></club_postlist>
      </el-tab-pane>
      <el-tab-pane label="已审核" name="Stared">
        <club_postlist type="Stared" user="CD"></club_postlist>
      </el-tab-pane>
      <el-tab-pane label="未通过" name="UnPassed">
        <club_postlist type="UnPassed" user="CD"></club_postlist>
      </el-tab-pane>
      <el-tab-pane label="所有" name="All">
        <club_postlist type="All" user="CD"></club_postlist>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>
<script>
  import PostList from '../../components/public/PostList.vue'
  export default {
    components: {
      'club_postlist': PostList
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
