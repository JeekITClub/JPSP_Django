from django.conf.urls import url

from . import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^club',views.club_fileupload,name='club_fileupload'),
    url(r'^admin/login',views.admin_login,name="login")
]