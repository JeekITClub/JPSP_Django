<template>
  <el-table :data="PostList" border style="width: 100%">
    <el-table-column type="expand">
      <template :scope="props">
        <el-table :label-position="left" inline>
          <el-table-item label="活动地点">
            <span>{{ props.row.Region }}</span>
          </el-table-item>
          <el-table-item label="活动内容">
            <span>{{ props.row.Content }}</span>
          </el-table-item>
          <el-table-item label="活动过程">
            <span>{{ props.row.Process }}</span>
          </el-table-item>
          <el-table-item label="活动评价">
            <span>{{ props.row.Assessment }}</span>
          </el-table-item>
          <el-table-item label="感悟分析">
            <span>{{ props.row.Feeling }}</span>
          </el-table-item>
        </el-table>
      </template>
    </el-table-column>
    <el-table-column label="PostID" width="100" prop="PostId">
      <span style="margin-left: 10px">{{ scope.row.pk }}</span>
    </el-table-column>
    <el-table-column label="社团" width="100">
      <span style="margin-left: 10px">{{ scope.row.ClubName }}</span>
    </el-table-column>
    <el-table-column label="联系人" width="100">
      <span style="margin-left: 10px">{{ scope.row.Linkman }}</span>
    </el-table-column>
    <el-table-column label="社团活动时间">
      <span style="margin-left: 10px">{{ scope.row.Date1 }}--{{ scope.row.Date2 }}</span>
    </el-table-column>
    <el-table-column label="评价">
      <template :scope=scope>
        <el-rate v-model="scope.row.Star" v-on:change="StarSubmit"></el-rate>
      </template>
    </el-table-column>
    <el-table-column label="操作">
      <el-button size="small" type="danger" @click="HandleDeleteSubmit(scope.$index,scope.row)">
        删除
      </el-button>
    </el-table-column>
  </el-table>
</template>

<script>
  import axios from 'axios'
  export default {
    data () {
      return {
        PostListTable: []
      }
    },
    methods: {
      StarSubmit (index, row, star) {
        axios({
          method: 'POST',
          url: '/api/cd/star/Submit',
          data: JSON.stringify({
            Stars: star,
            StarTime: '',
            // TODO: star_time
            PostId: '',
            // TODO: PostId
            Token: ''
          })
        })
      },
      HandleDeleteSubmit (index, row) {
        console.log(index, row)
        axios({
          method: 'POST',
          url: '/api/cd/Post/DeleteSubmit',
          data: JSON.stringify({
            HandleTime: '',
            // TODO: HandleTime
            PostId: '',
            // TODO: PostId
            Token: ''
          })
        })
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
      },
      PostList () {
        axios({
          method: 'GET',
          url: '/api/cd/post/list',
          data: JSON.stringify({
            Token: ''
          }).then(function (response) {
            if (response.data.message === 'error') {
              console.log('error')
            } else {
              console.log(response.data)
            }
          }.bind(this)).catch(function (error) {
            console.log(error)
          })
        })
      }
    }
  }
</script>
