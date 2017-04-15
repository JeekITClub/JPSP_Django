from django.conf.urls import url

from . import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^login/',views.login,name='login'),
    url(r'^admin/login',views.admin_login,name="admin_login"),
    url(r'^admin/',views.admin,name='admin'),
    url(r'^club/admin/file/success',views.club_admin_file_upload,name="club_admin_file_upload"),
    url(r'^club/admin/file',views.club_admin_file,name="club_admin_file"),
    url(r'^test/',views.test,name='test'),
    url(r'^allclub/',views.club_all,name='club_all'),
    url(r'^club/clubid',views.clubid,name='clubid'),
    #clubid的url匹配社团id
]