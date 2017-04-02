from django.conf.urls import url

from . import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^admin/login',views.admin_login,name="login"),
    url(r'^club/admin/file/success',views.club_admin_file_upload,name="club_admin_file_upload"),
    url(r'^club/admin/file',views.club_admin_file,name="club_admin_file"),
]