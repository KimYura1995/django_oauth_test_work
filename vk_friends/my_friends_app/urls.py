from django.urls import path

from my_friends_app.views import login_view, logout_view, list_friend_view


urlpatterns = [
    path('', login_view, name='login'),
    path('<slug:user_id>/', list_friend_view, name='friend_view'),
    path('<slug:user_id>/logout/', logout_view, name='logout')
]
