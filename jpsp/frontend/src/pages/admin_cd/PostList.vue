<template>
  <div>
    <el-tabs v-model="editableTabsValue2" type="card" closable @tab-remove="removeTab">
      <el-tab-pane label="excel" name="first">
        <cd_post_list></cd_post_list>
      </el-tab-pane>
      <el-tab-pane label="adw" name="fasd">
        <cd_post_list></cd_post_list>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>
<script>
  import PostList from '../../components/admin_cd/PostList.vue'
  export default {
    components: {
      'cd_post_list': PostList
    },
    data () {
      return {
        editableTabsValue2: 'first',
        editableTabs2: [{
          title: 'Tab 1',
          name: '1',
          content: ''
        }, {
          title: 'Tab 2',
          name: '2',
          content: 'Tab 2 content'
        }],
        tabIndex: 2
      }
    },
    methods: {
      addTab (targetName) {
        let newTabName = ++this.tabIndex + ''
        this.editableTabs2.push({
          title: 'New Tab',
          name: newTabName,
          content: 'New Tab content'
        })
        this.editableTabsValue2 = newTabName
      },
      removeTab (targetName) {
        let tabs = this.editableTabs2
        let activeName = this.editableTabsValue2
        if (activeName === targetName) {
          tabs.forEach((tab, index) => {
            if (tab.name === targetName) {
              let nextTab = tabs[index + 1] || tabs[index - 1]
              if (nextTab) {
                activeName = nextTab.name
              }
            }
          })
        }
        this.editableTabsValue2 = activeName
        this.editableTabs2 = tabs.filter(tab => tab.name !== targetName)
      }
    }
  }
</script>
<style>
</style>
