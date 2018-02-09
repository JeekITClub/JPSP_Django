from django.urls import path

from . import views

urlpatterns = [
    path(r's/logout', views.student_logout,name="StudentLogout"),
    path(r's/login', views.student_login_page,name="StudentLogin"),
    path('s/check_login',views.student_check_login,name="StudentCheckLogin"),
    path(r's/club/news/<int:page>', views.student_club_news),
    path(r's/club/list/<int:page>', views.student_club_list,name='StudentClubList'),
    path(r's/club/detail/<int:club_id>', views.student_club_detail,name="StudentClubDetail"),
    path(r's/club/establish', views.student_club_establish,name="StudentClubEstablish"),
    path(r's/dashboard', views.student_dashboard_index,name="StudentDashboardIndex"),
    path(r's/dashboard/password', views.student_dashboard_password),
    path(r's/dashboard/clubs', views.student_dashboard_clubs),
    path(r's/dashboard/activities', views.student_dashboard_activities),
    path(r'cd/login',views.admin_login_page,name="CDLogin"),
    path(r'c/login',views.club_login_page,name="ClubLogin"),
    path('', views.index)
]
