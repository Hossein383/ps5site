from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('Games/', views.listgames, name="ListGames"),
    path('Games/Details/<int:id>', views.detailsgame, name='Details'),
    path('login/', views.LoginUser, name='login'),
    path('Register/', views.Register, name='Register'),
    path('Logout/', views.logoutuser, name='logout'),

]
