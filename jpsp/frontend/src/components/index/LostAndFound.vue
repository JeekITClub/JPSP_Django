<template>
  <div>
    <el-form ref="form" :model="form">
      <el-form-item label="丢失或者捡到" :required=true>
        <el-radio label="Lost" v-model="form.LostOrFound">丢失</el-radio>
        <el-radio label="Found" v-model="form.LostOrFound">捡到</el-radio>
      </el-form-item>
      <el-form-item label="联系人" :required=true>
        <el-input v-model="form.LinkmanName" placeholder="联系人姓名"></el-input>
      </el-form-item>
      <el-form-item label="联系人年级" :required=true>
        <el-select v-model="form.LinkmanGrade" placeholder="请选择年级" value="">
          <el-option label="高一" value="1"></el-option>
          <el-option label="高二" value="2"></el-option>
          <el-option label="高三" value="3"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="联系人班级" :required=true>
        <el-select v-model="form.LinkmanClass" placeholder="请选择班级" value="">
          <el-option label="1" value="1"></el-option>
          <el-option label="2" value="2"></el-option>
          <el-option label="3" value="3"></el-option>
          <el-option label="4" value="4"></el-option>
          <el-option label="5" value="5"></el-option>
          <el-option label="6" value="6"></el-option>
          <el-option label="7" value="7"></el-option>
          <el-option label="8" value="8"></el-option>
          <el-option label="9" value="9"></el-option>
          <el-option label="10" value="10"></el-option>
          <el-option label="11" value="11"></el-option>
          <el-option label="12" value="12"></el-option>
          <el-option label="13" value="13"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="丢失物品名称" :required=true>
        <el-input v-model="form.ObjectName"></el-input>
      </el-form-item>
      <el-form-item label="联系人电话">
        <el-input v-model="form.LinkmanPhoneNumber" placeholder="请输入联系人电话"></el-input>
      </el-form-item>
      <el-form-item label="联系人QQ">
        <el-input v-model="form.LinkmanQq" placeholder="请输入联系人QQ"></el-input>
      </el-form-item>
      <el-form-item label="丢失区域" :required=true>
        <el-select v-model="form.Region" placeholder="请选择丢失区域" value="">
          <el-option label="挹芬楼" value="挹芬楼"></el-option>
          <el-option label="远翔楼" value="远翔楼"></el-option>
          <el-option label="致真楼" value="致真楼"></el-option>
          <el-option label="行政楼" value="行政楼"></el-option>
          <el-option label="济美楼" value="济美楼"></el-option>
          <el-option label="体育馆" value="体育馆"></el-option>
          <el-option label="弘渊楼" value="弘渊楼"></el-option>
          <el-option label="篮球场" value="篮球场"></el-option>
          <el-option label="足球场" value="足球场"></el-option>
          <el-option label="金苹果大道" value="金苹果大道"></el-option>
          <el-option label="食堂" value="食堂"></el-option>
          <el-option label="宿舍" value="宿舍"></el-option>
          <el-option label="思贤堂" value="思贤堂"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="丢失时间" :required=true>
        <el-col :span="11">
          <el-date-picker type="date" placeholder="选择日期" v-model="form.date1" style="width: 100%;"></el-date-picker>
        </el-col>
        <el-col class="line" :span="2">-</el-col>
        <el-col :span="11">
          <el-time-picker type="fixed-time" placeholder="选择时间" v-model="form.date2"
                          style="width: 100%;"></el-time-picker>
        </el-col>
      </el-form-item>
      <el-form-item label="重要物品" :required=true>
        <el-switch :on-text="" :off-text="" v-model="form.Importance"></el-switch>
      </el-form-item>
      <el-form-item label="物品描述" :required=true>
        <el-input type="textarea" v-model="form.desc"></el-input>
      </el-form-item>
      <el-form-item :required=true>
        <el-button type="primary" @click="onSubmit">立即创建</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>
<script>
  import axios from 'axios'
  export default {
    data () {
      return {
        form: {
          LostOrFound: '',
          ObjectName: '',
          Region: '',
          date1: '',
          date2: '',
          Importance: false,
          desc: '',
          LinkmanGrade: '',
          LinkmanName: '',
          LinkmanClass: '',
          LinkmanQq: '',
          LinkmanPhoneNumber: ''
        }
      }
    },
    methods: {
      onSubmit () {
        axios({
          method: 'POST',
          url: '/api/index/LAF/Submit',
          data: JSON.stringify({
            LostOrFound: this.LostOrFound,
            ObjectName: this.ObjectNameName,
            LinkmanName: this.LinkmanName,
            LinkmanGrade: this.LinkmanGrade,
            LinkmanPhoneNumber: this.LinkmanPhoneNumber,
            LinkmanQq: this.LinkmanQq,
            Region: this.Region,
            Date1: this.date1,
            Date2: this.date2,
            Importance: this.Importance,
            Desc: this.desc,
            Token: this.GetToken
          })
        }).then(function (response) {
          if (response.data.message === 'Error') {
            console.log('error')
          } else if (response.data.message === 'success') {
            console.log('success')
          }
        }).catch(function () {
          alert('error: PostEdit')
        })
      }
    },
    computed: {
      GetUserId () {
        return this.$cookie.get('UserId')
      },
      GetIndexToken () {
        return this.$cookie.get('IndexToken')
      },
      GetUserName () {
        return this.$cookie.get('UserName')
      },
      GetIndexAuthenticated () {
        return this.$cookie.get('IndexAuthenticated')
      },
      /**
       * @return {string}
       */
      GetApi () {
        return this.$store.state.Api
      }
    }
  }
</script>
