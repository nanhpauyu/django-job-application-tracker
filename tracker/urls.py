from django.urls import path
from .views import home, applications, add_post, login, logout, update_status

urlpatterns = [
    path('', home, name='home'),
    path('applications', applications, name='applications'),
    path('add_post', add_post, name='add_post'),
    path('login', login, name="login"),
    path('logout', logout, name='logout'),
    path('update_status/<int:pk>', update_status, name='update_status'),
]
