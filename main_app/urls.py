from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path('accounts/signup/', views.signup, name='signup'),
    path('chats/', views.chats_index, name="index"),
    path('chats/<int:pk>/delete/', views.ChatDelete.as_view(), name='chats_delete')
]
