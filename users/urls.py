from django.urls import path
from users.views import login_user,logout_user

urlpatterns = [
    path('login_user/',login_user,name="login"),
    path('logout_user/',logout_user,name='logout')
    
]
