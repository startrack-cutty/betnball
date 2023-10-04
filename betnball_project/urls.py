"""
URL configuration for betnball_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bets.views import get_user_bets
from billinginfo.views import get_billing_info
from jefftestapp.views import showUrls
# from main_app.views import index
from main_app2.views import index
from picks.views import get_user_picks
from pools.views import get_user_pools
from posts.views import get_posts
from sports.views import get_all_sports
from schedule.views import get_schedule
from teams.views import get_all_teams
from users.views import user_login, get_user, get_friends, get_all_users
from welcome.views import show_options


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="home"),
    path('bets/', get_user_bets, name="bets"),
    path('billing-info/', get_billing_info, name="billing"),
    path('welcome/', show_options, ),  # Page shown after user logs in.
    path('picks/', get_user_picks, ),
    path('pools/', get_user_pools, ),
    path('jefftestapp/', showUrls, ),
    path('friends/', get_friends, ),
    path('schedule/', get_schedule, name="schedule"),
    path('sports/', get_all_sports, ),
    path('teams/', get_all_teams, ),
    path('user-login/', user_login, ),
    path('user-login/<str:username>/<str:password>/', get_user, ),
    path('posts/', get_posts, ),
    path('users/', get_all_users, name="users"),
]
