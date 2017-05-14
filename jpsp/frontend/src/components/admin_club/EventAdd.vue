<el-form ref="form" :model="form" label-width="80px">
  <el-form-item label="活动名称">
    <el-input v-model="form.name"></el-input>
  </el-form-item>
  <el-form-item label="活动地点">
    <el-input v-model="form.region" placeholder="请输入活动地点" value="">
    </el-input>
  </el-form-item>
  <el-form-item label="活动时间">
    <el-col :span="11">
      <el-date-picker type="date" placeholder="选择日期" v-model="form.date1" style="width: 100%;"></el-date-picker>
    </el-col>
    <el-col class="line" :span="2">-</el-col>
    <el-col :span="11">
      <el-time-picker type="fixed-time" placeholder="选择时间" v-model="form.date2" style="width: 100%;"></el-time-picker>
    </el-col>
  </el-form-item>
  <!--<el-form-item label="即时配送">-->
    <!--<el-switch on-text="" off-text="" v-model="form.delivery"></el-switch>-->
  <!--</el-form-item>-->
  <el-form-item label="活动性质">
    <el-checkbox-group v-model="form.type">
      <el-checkbox label="" name="type"></el-checkbox>
      <el-checkbox label="" name="type"></el-checkbox>
      <el-checkbox label="" name="type"></el-checkbox>
      <el-checkbox label="" name="type"></el-checkbox>
    </el-checkbox-group>
  </el-form-item>
  <el-form-item label="特殊资源">
    <el-radio-group v-model="form.resource">
      <el-radio label="线上品牌商赞助"></el-radio>
      <el-radio label="线下场地免费"></el-radio>
    </el-radio-group>
  </el-form-item>
  <el-form-item label="活动形式">
    <el-input type="textarea" v-model="form.desc"></el-input>
  </el-form-item>
  <el-form-item>
    <el-button type="primary" @click="onSubmit">立即创建</el-button>
    <el-button>取消</el-button>
  </el-form-item>
</el-form>
<el-form :model="dynamicValidateForm" ref="dynamicValidateForm" label-width="100px" class="demo-dynamic">
  <el-form-item
    v-for="(achievement, index) in dynamicValidateForm.achievements"
    :label="'成就' + index"
    :key="achievement.key"
    :prop="'achievement.' + index + '.value'"
    :rules="{
      required: true, message: '不能为空', trigger: 'blur'
    }"
  >
    <el-input v-model="achievement.value"></el-input><el-button @click.prevent="removeAchievement(achievement)">删除</el-button>
  </el-form-item>
  <el-form-item>
    <el-button type="primary" @click="submitForm('dynamicValidateForm')">提交</el-button>
    <el-button @click="addAchievement">新增成就</el-button>
    <el-button @click="resetForm('dynamicValidateForm')">重置</el-button>
  </el-form-item>
</el-form>
<script>
  import ElInput from "../../../node_modules/element-ui/packages/input/src/input";
  export default {
    components: {ElInput},
    data() {
      return {
        form: {
          name: '',
          region: '',
          date1: '',
          date2: '',
          delivery: false,
          type: [],
          resource: '',
          desc: ''
        },
        dynamicVaildateForm:{
            achievements:[
              {
                  value:''
              }
            ],
          email:''
        }
      }
    },
    methods: {
      onSubmit() {
        console.log('submit!');
      },
      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            alert('submit!');
          } else {
            console.log('error submit!!');
            return false;
          }
        });
      },
      resetForm(formName) {
        this.$refs[formName].resetFields();
      },
      removeAchievement(item) {
        var index = this.dynamicValidateForm.ahievements.indexOf(item)
        if (index !== -1) {
          this.dynamicValidateForm.achievements.splice(index, 1)
        }
      },
      addAchievement() {
        this.dynamicValidateForm.ahievements.push({
          value: '',
          key: Date.now()
        });
      }
    }
  }
</script>
<style>
  @import url("//unpkg.com/element-ui@1.3.2/lib/theme-default/index.css");
</style>
