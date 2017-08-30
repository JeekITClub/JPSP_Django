<template>
  <div class="container">
    <div class="thumbnail">
      <div class="caption">
        <h3>{{ Activity.Name }}</h3>
        <p>
          <router-link :to="{ name: 'ActivityDetail', params: { ActivityId: this.$props.ActivityId }}">
            <button class="btn btn-primary" type="button">活动详情</button>
          </router-link>
        </p>
      </div>
    </div>
  </div>
</template>
<script>
  import axios from 'axios'
  export default {
    data () {
      return {
        Activity: {}
      }
    },
    prop: {
      ActivityId: {
        'default': '0'
      }
    },
    mounted: function () {
      axios({
        method: 'POST',
        url: this.GetApi + 'activity/detail/',
        data: JSON.stringify({
          ActivityId: this.$props.ActivityId
        }),
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
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
