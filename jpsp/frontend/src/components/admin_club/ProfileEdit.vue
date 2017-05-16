<el-form ref="form" :model="PostForm" label-width="80px">
  <el-form-item label="社团名称">
    <el-input v-model="PostForm.ClubName"></el-input>
  </el-form-item>
  <el-form-item label="">
  <el-input v-model="PostForm.ActivityName" placeholder="请输入活动名称"></el-input>
  </el-form-item>
  <el-form-item label="活动地点">
    <el-input v-model="PostForm.region" placeholder="请输入活动地点" value=""></el-input>
  </el-form-item>
  <el-form-item label="活动时间">
    Mel
  </el-form-item>
  <el-form-item
    v-for="(achievement, index) in PostForm.achievements"
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
    <el-button type="primary" @click="submitForm('PostForm')">提交</el-button>
    <el-button @click="addAchievement">新增成就</el-button>
    <el-button @click="resetForm('PostForm')">重置</el-button>
  </el-form-item>
  <el-form-item>
    <el-button type="primary" @click="onSubmit">立即创建</el-button>
    <el-button>取消</el-button>
  </el-form-item>
</el-form>
<script>
  import ElInput from '../../../node_modules/element-ui/packages/input/src/input'
  export default {
    components: {ElInput},
    data () {
      return {
        PostForm: {
          name: '',
          region: '',
          date1: '',
          date2: '',
          date3: '',
          type: [],
          resource: '',
          desc: '',
          introduction: '',
          achievements: [
            {
              value: ''
            }
          ]
        }
      }
    },
    methods: {
      onSubmit () {
        console.log('submit!')
      },
      submitForm (formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            alert('submit!')
          } else {
            console.log('error submit!!')
            return false
          }
        })
      },
      resetForm (formName) {
        this.$refs[formName].resetFields()
      },
      removeAchievement (item) {
        var index = this.dynamicValidateForm.achievements.indexOf(item)
        if (index !== -1) {
          this.dynamicValidateForm.achievements.splice(index, 1)
        }
      },
      addAchievement () {
        this.dynamicValidateForm.achievements.push({
          value: '',
          key: Date.now()
        })
      }
    }
  }
</script>
<style>
  @import url("//unpkg.com/element-ui@1.3.2/lib/theme-default/index.css");
</style>
