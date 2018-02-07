"""jpsp URL Configuration
"""

from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin', admin.site.urls)
    # path('jpsp', include('jpspapp.urls'))
]
