from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index,name='myapp'),
    path('register/',views.register,name='register'),
    path('otp/',views.otp,name='otp'),
    path('login/',views.login,name='login'),
    path('index/',views.index,name='index'),
    path('logout/',views.logout,name='logout'),
    path('forgot/',views.forgot,name='forgot'),
    path('change-password/',views.change_password,name='change-password'),
    path('profile',views.profile,name='profile'),
]