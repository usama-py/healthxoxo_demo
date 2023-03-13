
from django.urls import path,include
from website.views import expertTalk,welcome,signup,dietChart,monitorFast,get_and_delete_user_time,add_food_item,healthyHabits
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
urlpatterns = [
    # URL pattern for the home page
    path('', welcome, name='home'),
    # URL pattern for the expert talk page
    path('expertTalk/', expertTalk, name='expertTalk'),
    # URL pattern for the signup page
    path('signup/', signup, name='signup'),
    # URL patterns for authentication-related views provided by Django
    path('users/', include('django.contrib.auth.urls')),
    # URL pattern for the users app views
    path('users/', include('users.urls')),
    # URL pattern for the diet chart page
    path('dietChart/', dietChart, name='dietChart'),
    # URL pattern for the monitor fast page
    path('monitorFast/', monitorFast, name='monitorFast'),
    # URL pattern for the login page
    path('login_user/', LoginView.as_view(template_name='login.html'), name='login'),
    # URL pattern for the logout page
    path('logout_user/', LogoutView.as_view(next_page=reverse_lazy('home')), name='logout'),
    # URL pattern for the get_and_delete_user_time view
    path('get_and_delete_user_time', get_and_delete_user_time, name='get_and_delete_user_time'),
    # URL pattern for the add_food_item view
    path('food_tracker/', add_food_item, name='food_tracker'),
    # URL pattern for the healthy habits page
    path('healthyHabits/', healthyHabits, name='healthyHabits'),
]