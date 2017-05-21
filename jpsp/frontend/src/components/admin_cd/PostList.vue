<template>
  <el-table :data="PostListTable" border style="width: 100%">
    <el-table-column label="PostID" width="100">
      <template scope="scope">
        <span style="margin-left: 10px">{{ scope.row.id }}</span>
      </template>
    </el-table-column>
    <el-table-column label="社团" width="100">
      <span style="margin-left: 10px">{{ scope.row.clubname }}</span>
    </el-table-column>
    <el-table-column label="联系人" width="100">
      <span style="margin-left: 10px">{{ scope.row.linkman }}</span>
    </el-table-column>
    <el-table-column label="社团活动时间">
      <span style="margin-left: 10px">{{ scope.row.Date1 }}{{ scope.row.Date2 }}</span>
    </el-table-column>
    <el-table-column label="评价">
      <template scope="scope">
        <el-rate v-model="scope.row.star" v-on:change="StarSubmit"></el-rate>
      </template>
    </el-table-column>
    <el-table-column label="操作">
      <el-button size="small" type="danger" @click="HandleDeleteSubmit(scope.$index,scope.row)">
        删除
      </el-button>
    </el-table-column>
  </el-table>
  <el-dialog title="收货地址" :visible.sync="dialogTableVisible">

  </el-dialog>
</template>

<script>
  import ElButton from "../../../node_modules/element-ui/packages/button/src/button";
  export default {
    components: {ElButton},
    data() {
      return {
        PostListTable: [
          {
            Id: '',
            Clubname: '',
            Linkman: '',
            Region: '',
            Date1: '',
            Date2: '',
            Star: '',
            Content: '',
            Process: '',
            Assessment: '',
            Feeling: ''
          }
        ],
        dialogTableVisible: false
      }
    },
    methods: {
      StarSubmit (index, row) {
        console.log(index, row)
        axios({
          method: 'POST',
          url: '/api/cd/star/Submit',
          data: JSON.stringify({
            StarTime: date.now(),
            PostId: scope.$index.id,
            Token: ''
          })
        })
      },
      HandleDeleteSubmit (index, row) {
        console.log(index, row);
        axios({
          method: 'POST',
          url: '/api/cd/Post/DeleteSubmit',
          data: JSON.stringify({
            HandleTime: date.now(),
            PostId: scope.$index.id,
            Token: ''
          })
        })
      }
    }
  }
</script>
