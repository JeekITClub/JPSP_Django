<template>
  <div>
    <div class=""></div>
  </div>
</template>
<script>
  import axios from 'axios'
  import ActivityShow from '../../components/index/ActivityShow.vue'
  export default {
    components: {
      'activity_show': ActivityShow
    },
    data () {
      return {
        ActivityNum: 0
      }
    },
    methods: {},
    mounted: function () {
      axios({
        method: 'POST',
        url: this.GetApi + 'activit/count',
        data: null
      }).then(function (response) {
        if (response.data.message === 'success') {
          this.data.ActivityNum = JSON.parse(response.data.data.ActivityNum)
        } else {
          this.$notify.error({
            'title': '错误',
            'message': '获取活动消息错误'
          })
        }
      })
    },
    computed: {
      /**
       * @return {string}
       */
      GetApi () {
        return this.$store.state.Api
      }
    }
  }
</script>
<style>
</style>
