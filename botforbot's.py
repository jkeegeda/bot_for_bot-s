from vk_api.longpoll import VkLongPoll, VkEventType
from threading import Thread
import vk_api
import random
import time
import os


mytokenvk = os.environ.get('BOT_TOKEN_VK')
longpull = VkLongPoll(vk_session)
vk = vk_session.get_api()


def e_bot():
    while True:
        vk.messages.send(
                chat_id=48,
                message="Камень",
                random_id=random.randint(0, 10000000000000000)
        )
        time.sleep(20)

def gorilla():
    while True:
        for _ in range(5):
            vk.messages.send(
                chat_id=48,
                message="Копать железо",
                random_id=random.randint(0, 10000000000000000)
            )
            time.sleep(2)
        time.sleep(1505)

def main():
    e_Bot = Thread(target=e_bot)
    Gorilla = Thread(target=gorilla)
    e_Bot.start()
    Gorilla.start()


if __name__ == '__main__':
    main()

