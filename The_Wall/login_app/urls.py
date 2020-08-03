from django.urls import path
from . import views

urlpatterns = [
    path('login/registration', views.index), 
    path('register', views.create_user),
    path('login', views.login),
    path('login/registration',views.login),
    path('success/login', views.logged_in),
    path('success/registered', views.registered),
    path('log_out', views.log_out),
    path('wall', views.wall),
    path('message', views.post_message),
    path('add_comment/<int:id>', views.post_comment)

    
]