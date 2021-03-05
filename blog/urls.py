from django.urls import path
from .views import UpdatePost
from . import views


urlpatterns = [
    path('', views.blog, name='blog-home'),
    path('update/<int:pk>', UpdatePost.as_view(), name='update_page'),

]
