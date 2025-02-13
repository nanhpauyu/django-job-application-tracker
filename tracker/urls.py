from django.urls import path
from .views import home, application, add_post

urlpatterns = [
    path('', home, name='home'),
    path('application', application, name='application'),
    path('add_post',add_post, name='add_post')
]
