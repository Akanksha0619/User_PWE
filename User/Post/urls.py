from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_post, name='create_post'),
    path('', views.post_list, name='post_list'),
    path('<int:pk>/update/', views.update_post, name='update_post'),
    path('<int:pk>/delete/', views.delete_post, name='delete_post'),
]
