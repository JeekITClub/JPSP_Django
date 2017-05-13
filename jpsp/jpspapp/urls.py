from django.conf.urls import url

from . import views

urlpatterns=[
    url(r'^club_list',views.club_list,name='club_list'),
]
