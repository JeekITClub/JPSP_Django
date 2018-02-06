from django.urls import path

from . import views

urlpatterns = [
    path(r'^logout', views.logout),
    path(r'login', views.login_page),
    path(r'^post/operate', views.post_operate),
    path(r'^post/star', views.post_star),
    path(r'^post/submit', views.post_submit),
    # path(r'^activity/attend', views.activity_attend),
    # path(r'^activity/detail', views.activity_detail),
    # path(r'^activity/list', views.activity_list),
    # path(r'^activity/operate', views.activity_operate),
    path(r'^club/profile/submit', views.club_profile_submit),
    path(r'club/detail/<int:club_id>', views.club_detail_page),
    # path(r'^club/recruit/classroom/submit', views.recruit_classroom_apply),
    # path(r'^club/recruit/classroom/operate', views.recruit_classroom_operate),
    # path(r'^club/recruit/classroom/list', views.recruit_classroom_list),
    path(r'^user/profile/submit', views.userprofile_submit),
    path(r'^user/profile/get', views.userprofile_get),
    # path(r'^club/member/add', views.club_member_add),
    # path(r'^club/member/remove', views.club_member_remove),
    # path(r'^club/member/list/confirmed', views.club_confirmed_member_list),
    # path(r'^club/member/list/unconfirmed', views.club_unconfirmed_member_list),
    # path(r'^club/establish', views.club_establish),
    # path(r'^club/page', views.club_page),
    path(r'^club/attend', views.club_attend),
    path(r'^club/quit', views.club_quit),
    # path(r'^club/page/settings', views.club_page_setting),
    path(r'^post/list', views.post_list),
    path(r'^club/list', views.club_list),
    path(r'^club/show', views.student_club_show),
    #path(r'^club/file/download', views.club_list),
    #path(r'^cd/file/upload', views.cd_file_upload),
    path(r'^cd/file/download', views.club_list),
    path('^',views.index)
]
