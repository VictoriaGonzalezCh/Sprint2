from django.contrib import admin
from django.urls import path, include  # <- Asegúrate de importar include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sync_app.urls')),  # <- Esto incluye los URLs de tu app
]