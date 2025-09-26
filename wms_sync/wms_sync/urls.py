from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sync_app.urls')),
]