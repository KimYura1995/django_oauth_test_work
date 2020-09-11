from allauth.socialaccount.models import SocialToken
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from my_friends_app.vk_api_functions import _get_context_list_friends


def login_view(request):
    if request.user.is_authenticated:
        return redirect('friend_view', user_id=request.user)
    return render(request, 'my_friends_app/login.html')


def list_friend_view(request, user_id):
    access_token = SocialToken.objects.filter(account__user__username=user_id, account__provider='vk')
    first_name, last_name = request.user.get_full_name().split(' ')
    context = _get_context_list_friends(access_token)
    context['first_name'] = first_name
    context['last_name'] = last_name
    return render(request, 'my_friends_app/friend_list.html', context)


def logout_view(request, user_id):
    logout(request)
    return redirect('login')


