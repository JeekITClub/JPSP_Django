from django.urls import path

from . import views

urlpatterns = [
    path(r'logout', views.logout),
    path(r'login', views.login_page),
    path(r's/club/list/<int:page>', views.student_club_list),
    path(r's/club/detail/<int:club_id>',views.student_club_detail),
    path(r's/dashboard',views.student_dashboard_index),


    path('',views.index)
]
