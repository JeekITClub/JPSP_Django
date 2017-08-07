from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^logout',views.logout),
    url(r'^login', views.login),
    url(r'^post/operate', views.post_operate),
    url(r'^post/star', views.post_star),
    url(r'^post/submit', views.post_submit),
    url(r'^activity/attend', views.activity_attend),
    url(r'^activity/detail', views.activity_detail),
    url(r'^activity/list', views.activity_list),
    url(r'^activity/operate', views.activity_operate),
    url(r'^clubprofile/submit', views.clubprofile_submit),
    url(r'^clubprofile/get', views.clubprofile_get),
    url(r'^recruit/classroom/submit', views.recruit_classroom_apply),
    url(r'^recruit/classroom/operate', views.recruit_classroom_operate),
    url(r'^userprofile/submit', views.userprofile_submit),
    url(r'^userprofile/get', views.userprofile_get),
    url(r'^club/member/operate', views.club_member_operate),
    url(r'^club/establish',views.club_establish),
    url(r'^clubpage',views.club_page),
    url(r'^clubpage/settings', views.club_page_setting),
    url(r'^post/list',views.post_list),
    url(r'^clublist',views.club_list)
]
