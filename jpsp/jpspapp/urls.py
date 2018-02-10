from django.urls import path

from . import views

urlpatterns = [
    path('logout', views.student_logout,name="Logout"),
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
    path('c/login',views.club_login_page,name="ClubLogin"),
    path('c/check_login',views.club_check_login,name="ClubCheckLogin"),
    path('c/file/upload/list/<int:page>',views.club_file_upload_list,name="ClubFileUploadList"),
    path('c/file/download/list/<int:page>',views.club_file_download_list,name="ClubFileDownloadList"),
    path('c/file/upload',views.club_file_upload,name="ClubFileUpload"),
    path('cd/check_login',views.admin_check_login,name="CDCheckLogin"),
    path('cd/dashboard',views.admin_dashboard,name="CDDashboard"),
    path('cd/post/list/<int:page>',views.admin_post_list,name="CDPostList"),
    path('cd/event/list/<int:page>',views.admin_event_list,name="CDEventList"),
    path('cd/file/upload/list/<int:page>',views.admin_file_upload_list,name="CDFileUploadList"),
    path('cd/file/download/list/<int:page>',views.admin_file_download_list,name="CDFileDownloadList"),
    path('cd/file/upload',views.admin_file_upload,name="CDFileUpload"),
    path('', views.index,name="Index")
]
