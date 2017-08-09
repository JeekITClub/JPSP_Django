from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^logout', views.logout),
    url(r'^login', views.login),
    url(r'^post/operate', views.post_operate),
    url(r'^post/star', views.post_star),
    url(r'^post/submit', views.post_submit),
    url(r'^activity/attend', views.activity_attend),
    url(r'^activity/detail', views.activity_detail),
    url(r'^activity/list', views.activity_list),
    url(r'^activity/operate', views.activity_operate),
    url(r'^club/profile/submit', views.clubprofile_submit),
    url(r'^club/profile/get', views.clubprofile_get),
    url(r'^recruit/classroom/submit', views.recruit_classroom_apply),
    url(r'^recruit/classroom/operate', views.recruit_classroom_operate),
    url(r'^recruit/classroom/list', views.recruit_classroom_list),
    url(r'^userprofile/submit', views.userprofile_submit),
    url(r'^userprofile/get', views.userprofile_get),
    url(r'^club/member/add', views.club_member_add),
    url(r'^club/member/remove', views.club_member_remove),
    url(r'^club/member/list/confirmed', views.club_confirmed_member_list),
    url(r'^club/member/list/unconfirmed', views.club_unconfirmed_member_list),
    url(r'^club/establish', views.club_establish),
    url(r'^clubpage', views.club_page),
    url(r'^clubpage/settings', views.club_page_setting),
    url(r'^post/list', views.post_list),
    url(r'^club/list', views.club_list)
]
