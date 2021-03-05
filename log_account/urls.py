from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_sys, name='login'),
    path('logout/', views.logout_sys, name='logout',)


]