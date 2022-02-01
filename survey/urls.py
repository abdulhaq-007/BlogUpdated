from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
app_name = 'survey'

urlpatterns = [
  path('', views.homeView, name='home'),
  path("detail/<slug:post_slug>", views.postDetail, name='post_detail'),
  path("category/<slug>/", views.categoryDetail, name='category_detail'),
  path('register/', views.RegisterView.as_view(), name='register'),
  path('login/', auth_views.LoginView.as_view(template_name='survey/login.html'), name='login'),
  path('profile/', views.ProfileView.as_view(), name='profile'),
  path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]    