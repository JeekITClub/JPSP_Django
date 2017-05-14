<template>

</template>
<script>
  export default {
    data () {
      return {
        PostForm: {
          ClubName: '',
          Linkman: {
            Grade: '',
            Class: '',
            Name: '',
            PhoneNumber: '',
            Qq: ''
          },
          Region: '',
          Date1: '',
          Date2: '',
          Content: '',
          Process: '',
          Assessment: '',
          Feeling: ''
        },
        rules: {
          ClubName: [
            {required: true, message: '请输入社团名称', trigger: 'blur'}
          ],
          Region: [
            {required: true, message: '请选择活动区域', trigger: 'change'}
          ],
          Date1: [
            {type: 'date', required: true, message: '请选择日期', trigger: 'change'}
          ],
          Date2: [
            {type: 'date', required: true, message: '请选择时间', trigger: 'change'}
          ]

        }
      }
    },
    methods: {
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
      }
    }
  }
</script>
<style>

</style>
