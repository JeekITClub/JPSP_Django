from django.conf.urls import url

from . import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^login/',views.login,name='login'),
    url(r'^admin/stars/overview',views.admin_stars_overview,name='admin_stars_overview'),
    url(r'^admin/post/overview',views.admin_post_overview,name="admin_post_overview"),
    url(r'^admin/post/edit',views.admin_post_edit,name="admin_post_edit"),
    url(r'^admin/post/verify',views.admin_post_verify,name='admin_post_verify'),
    url(r'^admin/post/denied',views.admin_post_denied,name="admin_post_denied"),
    url(r'^admin/post/analysis',views.admin_post_analysis,name="admin_post_analysis"),
    url(r'^admin/login',views.admin_login,name="admin_login"),
    url(r'^admin/',views.admin,name='admin'),
    url(r'^club/admin/file/success',views.club_admin_file_upload,name="club_admin_file_upload"),
    url(r'^club/admin/file',views.club_admin_file,name="club_admin_file"),
    url(r'^test/',views.test,name='test'),
    url(r'^wto_test',views.wto_test,name="wto_test"),
    url(r'^allclub/',views.club_all,name='club_all'),
    url(r'^club/clubid',views.clubid,name='clubid'),
    #clubid的url匹配社团id
]
