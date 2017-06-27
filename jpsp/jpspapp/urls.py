from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^club_list', views.club_list),
    url(r'^loginout',views.logout),
    url(r'^login', views.login),
    url(r'^club/post/edit/submit', views.club_post_edit_submit),
    url(r'^cd/post/deny/submit', views.cd_post_deny_submit),
    url(r'^cd/post/star/submit', views.cd_post_star_submit),
    url(r'^club/profile/edit/submit', views.club_profile_edit_submit),
    url(r'^club/profile/get', views.club_profile_get),
    url(r'^club/recruit/classroom/apply/submit', views.club_recruit_classroom_apply_submit,),
    url(r'^cd/recruit/classroom/apply/verify', views.cd_recruit_classroom_apply_verify_submit,),
    url(r'^user/profile/edit/submit', views.user_profile_edit_submit),
    url(r'^club/member/add/submit', views.club_member_add_submit),
    url(r'^club/member/remove/submit', views.club_member_remove_submit),
    url(r'^cd/message/list', views.cd_message_list),
    url(r'^cd/message/remove/submit', views.cd_message_remove_submit),
    url(r'^club/activity/apply/submit', views.club_activity_apply_submit),
    url(r'^cd/activity/agree/submit', views.cd_activity_agree_submit),
    url(r'^cd/activity/deny/submit', views.cd_activity_deny_submit),
    url(r'^cd/activity/list', views.cd_activity_list),
    url(r'^cd/post/list',views.cd_post_list),
    url(r'^index/LAF/submit',views.lost_and_found_submit),
    url(r'^index/profile/get',views.user_profile_get),
    url(r'^public/club/list',views.club_list)
]
