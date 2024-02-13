from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),  
    path('get_users/', views.getUsers, name='get_users'),  
    path('read/<str:pk>/', views.getUser, name='get_user'),  
    path('create/', views.addUser, name='add_user'),  
    path('update/<str:pk>/', views.updateUser, name='update_user'),  
    path('delete/<str:pk>/', views.deleteUser, name='delete_user'),  

    # path('accounts/google/redirect/', views.google_login_redirect, name='google_login_redirect'), #DY
]
