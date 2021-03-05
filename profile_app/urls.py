from django.urls import path
from .views import UpdateProfile
from . import views


urlpatterns = [
    path('', views.profile, name='profile_page'),
    path('add_profile/', views.add_my_profile, name='add_profile'),
    path('updateProfile/<int:pk>/', UpdateProfile.as_view(), name='edit_profile'),


]
