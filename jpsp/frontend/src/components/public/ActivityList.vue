<template>
  <el-table :data=PostListTable>
    <el-table-column type="expand">
      <template scope="props">
        <el-form inline class="demo-table-expand">
          <el-row class="tac">
            <el-col :span="24">
              <el-form-item label="活动内容">
                <span>{{ props.row.Content }}</span>
              </el-form-item>
            </el-col>
            <el-col :span="24">
              <el-form-item label="活动过程">
                <span>{{ props.row.Process }}</span>
              </el-form-item>
            </el-col>
          </el-row>
        </el-form>
      </template>
    </el-table-column>
    <el-table-column prop="ActivityId" label="活动序号">
    </el-table-column>
    <el-table-column prop="Name" label="活动名称">
    </el-table-column>
    <el-table-column prop="ClubName" label="负责社团">
    </el-table-column>
    <el-table-column prop="Date1" label="开始日期">
    </el-table-column>
    <el-table-column prop="Date2" label="结束时间">
    </el-table-column>
    <el-table-column prop="Region" label="活动地点">
    </el-table-column>
    <el-table-column label="操作">
      <template scope="scope">
        <el-button size="small" type="danger" @click="HandleDeleteSubmit(scope.row.pk)">
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
    props: {
      type: {
        'default': 'UnStared'
      },
      user: {
        'default': 'Student'
      }
    },
    methods: {
      HandleDeleteSubmit (postid) {
        axios({
          method: 'POST',
          url: 'empty',
          data: JSON.stringify({
            // TODO: HandleTime
            PostId: postid,
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
    mounted: function () {
      axios({
        method: 'POST',
        url: 'http://127.0.0.1:8000/api/cd/post/list',
        data: JSON.stringify({
          Type: this.type,
          Token: this.GetToken
        })
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
