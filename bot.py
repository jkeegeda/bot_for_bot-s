from vk_api.longpoll import VkLongPoll, VkEventType
from threading import Thread
import vk_api
import random
import time
import os


mytokenvk = os.environ.get('BOT_TOKEN_VK')
vk_session = vk_api.VkApi(token=mytokenvk)
longpull = VkLongPoll(vk_session)
vk = vk_session.get_api()


# def e_bot():
#     while True:
#         vk.messages.send(
#                 chat_id=48,
#                 message="Камень",
#                 random_id=random.randint(0, 10000000000000000)
#         )
#         time.sleep(20)

def gorilla():
    while True:
        for _ in range(5):
            vk.messages.send(
                chat_id=48,
                message="Копать золото",
                random_id=random.randint(0, 10000000000000000)
            )
            time.sleep(2)
        time.sleep(1505)
        
def lion():
    while True:
        vk.messages.send(
                chat_id=45,
                message="Работать",
                random_id=random.randint(0, 10000000000000000)
        )
        time.sleep(91)

def main():
    #e_Bot = Thread(target=e_bot)
    Gorilla = Thread(target=gorilla)
    Lion = Thread(target=lion)
    #e_Bot.start()
    Gorilla.start()
    Lion.start()


if __name__ == '__main__':
    main()

