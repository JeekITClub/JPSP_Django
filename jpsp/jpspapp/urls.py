from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^club_list', views.club_list, name='club_list'),
    url(r'^loginout',views.logout, name='logout'),
    url(r'^login', views.login, name='login'),
    url(r'^club/post/EditSubmit', views.club_post_edit_submit, name='ClubPostEditSubmit'),
    url(r'^cd/post/DeleteSubmit', views.cd_post_delete_submit, name='CDPostDeleteSubmit'),
    url(r'^cd/post/StarSubmit', views.cd_post_star_submit, name='CDPostStarSubmit'),
    url(r'^club/profile/EditSubmit', views.club_profile_edit_submit, name="ClubProfileEditSubmit"),
    url(r'^club/recruit/classroom/ApplySubmit', views.club_recruit_classroom_apply_submit,
        name="ClubRecruitClassroomApplySubmit"),
    url(r'^cd/recruit/classroom/Apply/Verify', views.cd_recruit_classroom_apply_verify_submit,
        name="CDRecruitClassroomApplyVerifySubmit"),
    url(r'^user/profile/EditSubmit', views.user_profile_edit_submit),
    url(r'^club/member/AddSubmit', views.club_member_add_submit),
    url(r'^club/memeber/RemoveSubmit', views.club_member_remove_submit),
    url(r'^cd/message/List', views.cd_message_list),
    url(r'^cd/message/RemoveSubmit', views.cd_message_remove_submit),
    url(r'^club/activity/ApplySubmit', views.club_activity_apply_submit),
    url(r'^cd/activity/AgreeSubmit', views.cd_activity_agree_submit),
    url(r'^cd/activity/DisagreeSubmit', views.cd_activity_disagree_submit),
    url(r'^cd/post/list',views.cd_post_list)
]
