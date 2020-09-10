from vk_api import VkApi


def _get_context_list_friends(access_token):
    vk = VkApi(token=access_token)
    vk_methods = vk.get_api()
    json_friends = vk_methods.friends.get(order='random', count=5, fields=['nickname', 'photo_100'])
    context = dict(friends=json_friends['items'])
    return context
