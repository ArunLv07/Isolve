from django.urls import path
from .views import Register,Login,Home,MyPosts,AddPost,EditPost,DeletePost,Logout,Dashboard

urlpatterns = [
    path('',Dashboard.as_view(),name='dashboard'),
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('home/',Home.as_view(),name='home'),
    path('myposts/',MyPosts.as_view(),name='myposts'),
    path('add_post/',AddPost.as_view(),name='add_post'),
    path('edit_post/<int:id>',EditPost.as_view(),name='edit_post'),
    path('delete_post/<int:id>',DeletePost.as_view(),name='delete_post'),
]