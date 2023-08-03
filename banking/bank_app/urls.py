
from django.urls import path
from . import views

app_name = 'bank_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('new_page/', views.new_page, name='new_page'),
    path('logout/', views.logout, name='logout'),
    path('get/', views.get, name='get'),
    path('success/', views.success, name='success'),

]
