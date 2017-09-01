<template>
  <div>
    <div class="field">
      <label class="label">届数</label>
      <div class="control">
        <input class="input" type="number" placeholder="" v-model="Grade">
      </div>
    </div>
    <h2 class="title is-3">请依次输入各班人数以批量创建用户</h2>
    <hr>
    <div class="field">
      <label class="label">1</label>
      <div class="control">
        <input class="input" type="number" placeholder="" v-model="One">
      </div>
    </div>
    <div class="field">
      <label class="label">2</label>
      <div class="control">
        <input class="input" type="number" placeholder="" v-model="Two">
      </div>
    </div>
    <div class="field">
      <label class="label">3</label>
      <div class="control">
        <input class="input" type="number" placeholder="" v-model="Three">
      </div>
    </div>
    <div class="field">
      <label class="label">4</label>
      <div class="control">
        <input class="input" type="number" placeholder="" v-model="Four">
      </div>
    </div>
    <div class="field">
      <label class="label">5</label>
      <div class="control">
        <input class="input" type="number" placeholder="" v-model="Five">
      </div>
    </div>
    <div class="field">
      <label class="label">6</label>
      <div class="control">
        <input class="input" type="number" placeholder="" v-model="Six">
      </div>
    </div>
    <div class="field">
      <label class="label">7</label>
      <div class="control">
        <input class="input" type="number" placeholder="" v-model="Seven">
      </div>
    </div>
    <div class="field">
      <label class="label">8</label>
      <div class="control">
        <input class="input" type="number" placeholder="" v-model="Eight">
      </div>
    </div>
    <div class="field">
      <label class="label">9</label>
      <div class="control">
        <input class="input" type="number" placeholder="" v-model="Nine">
      </div>
    </div>
    <div class="field">
      <label class="label">10</label>
      <div class="control">
        <input class="input" type="number" placeholder="" v-model="Ten">
      </div>
    </div>
    <div class="field">
      <label class="label">11</label>
      <div class="control">
        <input class="input" type="number" placeholder="" v-model="Eleven">
      </div>
    </div>
    <div class="field">
      <label class="label">12</label>
      <div class="control">
        <input class="input" type="number" placeholder="" v-model="Twelve">
      </div>
    </div>
    <div class="field">
      <label class="label">13</label>
      <div class="control">
        <input class="input" type="number" placeholder="" v-model="Thirteen">
      </div>
    </div>
    <div class="control">
      <button class="button is-primary" @click="onSubmit">创建</button>
    </div>
  </div>
</template>
<script>
  import axios from 'axios'
  import Qs from 'qs'
  export default {
    data () {
      return {
        One: '',
        Two: '',
        Three: '',
        Four: '',
        Five: '',
        Six: '',
        Seven: '',
        Eight: '',
        Nine: '',
        Ten: '',
        Eleven: '',
        Twelve: '',
        Thirteen: '',
        Year: ''
      }
    },
    computed: {
      GetUserId () {
        return this.$cookie.get('CDUserId')
      },
      GetCDToken () {
        return this.$cookie.get('CDToken')
      },
      GetUserName () {
        return this.$cookie.get('CDUserName')
      },
      GetCDAuthenticated () {
        return this.$cookie.get('CDAuthenticated')
      },
      /**
       * @return {string}
       */
      GetApi () {
        return this.$store.state.Api
      }
    },
    methods: {
      onSubmit () {
        axios({
          method: 'POST',
          url: this.GetApi + 'profile',
          // TODO: API
          data: Qs.stringify({
//            Token: this.GetCDToken,
            ClassMember: [this.One, this.Two, this.Three, this.Four, this.Five, this.Six, this.Seven, this.Eight, this.Nine, this.Ten, this.Eleven, this.Twelve, this.Thirteen],
            Grade: this.Year
          }),
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
          }
        })
          .then(function (response) {
            if (response.data.message === 'success') {
              this.$notify.success({
                title: '成功',
                message: '创建成功'
              })
              console.log('success')
            } else {
              this.$notify.error({
                title: '错误',
                message: '创建失败'
              })
              console.log('error')
            }
          }.bind(this))
      }
    }
  }
</script>
<style>
</style>
