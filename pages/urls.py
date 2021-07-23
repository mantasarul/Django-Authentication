from django.urls.conf import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
]