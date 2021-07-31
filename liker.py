import vk_api
from time import sleep
from random import randint

login, password = 
vk_session = vk_api.VkApi(login, password)
vk_session.auth()
vk = vk_session.get_api()


def get_liked(post_id):
    if not check_like(post_id):
        sleep(4)
        vk_session.method('likes.add',
                          {'user_id': 353313939, 'type': 'post', 'owner_id': -193376219, 'item_id': post_id})


def check_like(post_id):
    a = vk_session.method('likes.isLiked',
                          {'user_id': 353313939, 'type': 'post', 'owner_id': -193376219, 'item_id': post_id})
    return a['liked']


def get_last_post_id():
    all_wall = (vk_session.method('wall.get', {'owner_id': -193376219, 'count': 2})).values()
    last_post_id = (list(list(all_wall)[1])[1])['id']
    return last_post_id


while True:
    last_post_id = get_last_post_id()
    get_liked(last_post_id)
    sleep(20 + randint(0, 10))
