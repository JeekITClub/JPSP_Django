from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^club_list', views.club_list),
    url(r'^loginout',views.logout),
    url(r'^login', views.login),
    url(r'^post/edit/', views.post_submit),
    url(r'^post/operate', views.post_operate),
    url(r'^post/star/submit', views.post_star),
    url(r'^clubprofile/submit', views.clubprofile_submit),
    url(r'^clubprofile/get', views.clubprofile_get),
    url(r'^recruit/classroom/apply/submit', views.recruit_classroom_apply_submit,),
    url(r'^cd/recruit/classroom/apply/verify', views.cd_recruit_classroom_apply_verify_submit,),
    url(r'^user/profile/edit/submit', views.user_profile_edit_submit),
    url(r'^club/member/add/submit', views.club_member_add_submit),
    url(r'^club/member/remove/submit', views.club_member_remove_submit),
    url(r'^cd/message/list', views.cd_message_list),
    url(r'^cd/message/remove/submit', views.cd_message_remove_submit),
    url(r'^club/activity/apply/submit', views.club_activity_apply_submit),
    url(r'^club/activity/list', views.club_activity_list),
    url(r'^cd/activity/agree/submit', views.cd_activity_agree_submit),
    url(r'^cd/activity/deny/submit', views.cd_activity_deny_submit),
    url(r'^cd/activity/list', views.cd_activity_list),
    url(r'^cd/post/list',views.cd_post_list),
    url(r'^index/LAF/submit',views.lost_and_found_submit),
    url(r'^index/profile/get',views.user_profile_get),
    url(r'^public/clublist',views.club_list)
]
