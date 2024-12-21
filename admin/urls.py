from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('reports/', include('report.urls')),
    path('', include('users.urls')),
    path('', include('dashboard.urls')),
    path('', include('advertisement.urls')),
]
