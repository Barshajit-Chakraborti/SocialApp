from django.urls import path
from . import views

urlpatterns = [
    # Feed
    path('', views.feed, name='feed'),

    # Authurization
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # Posts
    path('post/create/', views.create_post, name='create_post'),
    path('post/like/<int:post_id>/', views.like_post, name='like_post'),
    path('post/comment/<int:post_id>/', views.add_comment, name='add_comment'),
    path('post/edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('post/delete/<int:post_id>/', views.delete_post, name='delete_post'),

    # Profile
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/<str:username>/', views.profile, name='profile'),

    # Follow
    path('follow/<str:username>/', views.follow, name='follow'),

    # Search
    path('search/', views.search, name='search'),

    # Notifications
    path('notifications/', views.notifications, name='notifications'),
]