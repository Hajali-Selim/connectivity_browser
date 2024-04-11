from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name = 'datasets'

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path('', views.main, name='main'),
    path('<slug:slug>', views.description, name='description'),
    path('test/', views.testing_page, name='testing_page'),
    path('sentry-debug/', trigger_error),
] + staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
