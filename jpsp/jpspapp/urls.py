from django.urls import path

from . import views

urlpatterns = [
    path(r'logout', views.logout),
    path(r'login', views.login_page),
    path(r's/club/news/<int:page>', views.student_club_news),
    path(r's/club/list/<int:page>', views.student_club_list),
    path(r's/club/detail/<int:club_id>', views.student_club_detail),
    path(r's/club/establish', views.student_club_establish,name="StudentClubEstablish"),
    path(r's/dashboard', views.student_dashboard_index),
    path(r's/dashboard/password', views.student_dashboard_password),
    path(r's/dashboard/clubs', views.student_dashboard_clubs),
    path(r's/dashboard/activities', views.student_dashboard_activities),
    path(r'a/login', views.admin_login_page),
    path('', views.index)
]
