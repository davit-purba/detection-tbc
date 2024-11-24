from views.views import index, detect_image
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('detect', detect_image, name='detect_image'),
]
