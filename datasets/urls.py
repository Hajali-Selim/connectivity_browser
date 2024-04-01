from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name = 'datasets'
urlpatterns = [
    path('', views.main, name='main'),
    path('<slug:slug>', views.description, name='description'),
    #path('<int:id>', views.description, name='description'),
] + staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
