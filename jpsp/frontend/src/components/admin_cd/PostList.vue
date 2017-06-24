<template>
  <el-table :data=PostListTable>
    <el-table-column type="expand">
      <template scope="props">
        <el-form inline class="demo-table-expand">
          <el-row class="tac">
            <el-col :span="6">
              <el-form-item label="活动内容">
                <span>{{ props.row.Content }}</span>
              </el-form-item>
            </el-col>
            <el-col :span="6">
              <el-form-item label="活动过程">
                <span>{{ props.row.Process }}</span>
              </el-form-item>
            </el-col>
            <el-col :span="6">
              <el-form-item label="活动评价">
                <span>{{ props.row.Assessment }}</span>
              </el-form-item>
            </el-col>
            <el-col :span="6">
              <el-form-item label="感悟分析">
                <span>{{ props.row.Feeling }}</span>
              </el-form-item>
            </el-col>
          </el-row>
        </el-form>
      </template>
    </el-table-column>
    <el-table-column prop="pk" label="PostId">
    </el-table-column>
    <el-table-column prop="ClubName" label="社团名称">
    </el-table-column>
    <el-table-column prop="LinkmanName" label="联系人">>
    </el-table-column>
    <el-table-column prop="Date1" label="社团活动日期">
    </el-table-column>
    <el-table-column prop="Date2" label="社团活动时间">
    </el-table-column>
    <el-table-column prop="Region" label="活动地点">
    </el-table-column>
    <el-table-column prop="Stars" label="评价">
    </el-table-column>
    <el-table-column label="评价">
      <template scope="scope">
        <el-rate v-on:change="StarSubmit"></el-rate>
        <!--TODO: EL RATE function and its parameters-->
      </template>
    </el-table-column>
    <el-table-column label="操作">
      <template scope="scope">
        <el-button size="small" type="danger" @click="HandleDeleteSubmit(scope.$index,scope.row)">
          删除
        </el-button>
      </template>
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
      }
    },
//    mounted: {
//      PostList () {
//        axios({
//          method: 'GET',
//          url: '/api/cd/post/list',
//          data: JSON.stringify({
//            Token: ''
//          }).then(function (response) {
//            if (response.data.message === 'error') {
//              console.log('error')
//            } else if (response.data.message === 'success') {
//              console.log('success')
//            }
//          }.bind(this)).catch(function (error) {
//            console.log(error)
//          })
//        })
//      }
//    }
    mounted: function () {
      axios({
        method: 'GET',
        url: 'http://127.0.0.1:8000/api/cd/post/list'
      })
        .then(function (response) {
          if (response.data.message === 'success') {
            this.PostListTable = JSON.parse(response.data.data)
            console.log('success')
          } else {
            console.log('error')
          }
        }.bind(this))
    }
  }
</script>
