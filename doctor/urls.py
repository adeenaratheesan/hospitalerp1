
from django.urls import path
from . import views
app_name='doctor'

urlpatterns = [
    path('',views.index, name='index'),
    path('login',views.login, name='login'),
    path('register',views.register, name='register'),
    path('css',views.css,name='css'),
]