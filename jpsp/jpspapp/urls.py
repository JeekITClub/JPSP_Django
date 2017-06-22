from django.conf.urls import url

sfrom . import views

urlpatterns = [
    url(r'^club_list', views.club_list),
    url(r'^loginout',views.logout),
    url(r'^login', views.login),
    url(r'^club/post/EditSubmit', views.club_post_edit_submit),
    url(r'^cd/post/DenySubmit', views.cd_post_deny_submit),
    url(r'^cd/post/StarSubmit', views.cd_post_star_submit),
    url(r'^club/profile/EditSubmit', views.club_profile_edit_submit),
    url(r'^club/recruit/classroom/ApplySubmit', views.club_recruit_classroom_apply_submit,),
    url(r'^cd/recruit/classroom/Apply/Verify', views.cd_recruit_classroom_apply_verify_submit,),
    url(r'^user/profile/EditSubmit', views.user_profile_edit_submit),
    url(r'^club/member/AddSubmit', views.club_member_add_submit),
    url(r'^club/memeber/RemoveSubmit', views.club_member_remove_submit),
    url(r'^cd/message/List', views.cd_message_list),
    url(r'^cd/message/RemoveSubmit', views.cd_message_remove_submit),
    url(r'^club/activity/ApplySubmit', views.club_activity_apply_submit),
    url(r'^cd/activity/AgreeSubmit', views.cd_activity_agree_submit),
    url(r'^cd/activity/DenySubmit', views.cd_activity_deny_submit),
    url(r'^cd/post/list',views.cd_post_list),
    url(r'^index/LAF/Submit',views.lost_and_found_submit)
]
