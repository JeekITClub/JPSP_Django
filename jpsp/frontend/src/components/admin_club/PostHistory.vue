<template>
  <el-table :data="PostHitoryTable" border style="width: 100%">
    <el-table-column type="expand">
      <template scope="props">
        <el-form label-position="left" inline class="demo-table-expand">
          <el-form-item label="活动地点">
            <span>{{ props.row.Region }}</span>
          </el-form-item>
          <el-form-item label="活动内容">
            <span>{{ props.row.Content }}</span>
          </el-form-item>
          <el-form-item label="活动过程">
            <span>{{ props.row.Process }}</span>
          </el-form-item>
          <el-form-item label="活动评价">
            <span>{{ props.row.Assessment }}</span>
          </el-form-item>
          <el-form-item label="感悟分析">
            <span>{{ props.row.Feeling }}</span>
          </el-form-item>
        </el-form>
      </template>
    </el-table-column>
    <el-table-column label="PostID" width="100">
      <template scope="scope">
        <span style="margin-left: 10px">{{ scope.row.id }}</span>
      </template>
    </el-table-column>
    <el-table-column label="社团活动时间">
      <span style="margin-left: 10px">{{ scope.row.Date1 }}--{{ scope.row.Date2 }}</span>
    </el-table-column>
    <el-table-column label="评价">
      <template scope="scope">
        <el-rate v-bind="scope.row.Star"></el-rate>
      </template>
    </el-table-column>
  </el-table>
</template>
<script>
  export default {
    data () {
      return {
        PostHistoryTable: [
          {
            PostId: '',
            ClubName: '',
            Region: '',
            Date1: '',
            Date2: '',
            Star: '',
            Content: '',
            Process: '',
            Assessment: '',
            Feeling: ''
          }
        ]
      }
    }
  }
</script>
<style>
</style>
