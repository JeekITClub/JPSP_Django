<template>
  <el-table :data="ClubListTable" stripe style="width: 100%">
    <el-table-column type="expand">
      <template scope="props">
        <el-form inline class="demo-table-expand">
          <el-row class="tac">
            <el-col :span="24">
              <el-form-item label="招新QQ群">
                <span>{{ props.row.EnrollGroupQQ }}</span>
              </el-form-item>
            </el-col>
            <el-col :span="24">
              <el-form-item label="社团邮箱">
                <span>{{ props.row.Email }}</span>
              </el-form-item>
            </el-col>
            <el-col :span="24">
              <el-form-item label="社团介绍">
                <span>{{ props.row.Introduction }}</span>
              </el-form-item>
            </el-col>
            <el-col :span="24">
              <el-form-item label="成就">
                <span>{{ props.row.Achievements }}</span>
              </el-form-item>
            </el-col>
          </el-row>
        </el-form>
      </template>
    </el-table-column>
    <el-table-column prop="ClubId" label="社团Id"></el-table-column>
    <el-table-column prop="ShezhangName" label="社长姓名"></el-table-column>
    <el-table-column prop="ShezhangGrade" label="社长年级"></el-table-column>
    <el-table-column prop="ShezhangClass" label="社长班级"></el-table-column>
    <el-table-column prop="ShezhangQQ" label="社长QQ"></el-table-column>
    <el-table-column prop="IfRecruit" label="是否招新"></el-table-column>
    <el-table-column prop="State" label="是否已通过"></el-table-column>
    <el-table-column prop="Stars" label="评分"></el-table-column>
  </el-table>
</template>

<script>
  import axios from 'axios'
  export default {
    data () {
      return {
        ClubListTable: []
      }
    },
    mounted: function () {
      axios({
        method: 'POST',
        url: 'http://127.0.0.1:8000/api/public/club/list',
        data: JSON.stringify({
          Token: this.GetToken
        })
      }).then(function (response) {
        if (response.data.message === 'success') {
          this.ClubListTable = JSON.parse(response.data.data)
          console.log('success')
        } else {
          console.log('error')
        }
      }.bind(this))
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
    }
  }
</script>
<style>
  @import url("//unpkg.com/element-ui@1.3.2/lib/theme-default/index.css");
</style>
