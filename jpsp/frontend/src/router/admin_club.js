/**
 * Created by wto on 2017/5/12 0012.
 */
import Vue from 'vue'
import Router from 'vue-router'
import index from '@/pages/admin_club/index.vue'
import PostEdit from '@/pages/admin_club/PostEdit.vue'
import ProfileEdit from '@/pages/admin_club/ProfileEdit.vue'
import ActivityApply from '@/pages/admin_club/ActivityApply.vue'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: index
    },
    {
      path: '/post',
      name: 'Post',
      component: PostEdit,
      children: [
        {
          path: '/edit',
          name: 'PostEdit',
          component: PostEdit
        }
      ]
    },
    {
      path: '/profile',
      name: 'Profile',
      component: ProfileEdit
    },
    {
      path: '/activity',
      name: 'Activity',
      component: ActivityApply,
      children: [
        {
          path: '/apply',
          name: 'ActivityApply',
          component: ActivityApply
        }
      ]
    }
  ]
})
