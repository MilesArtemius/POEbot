import telepot
import urllib3

import system.api


class TelegramApi(system.api.Api):
    def __init__(self):
        super().__init__()
        self.bot = telepot.Bot('710918583:AAH6GxWYjn7TRDAcqQ60OBv40T32iUZUwjY')

    def get_user_id(self, message):
        return ""

    def send_message(self, message, user_id, attachment, token):
        pass

    def get_message_text(self, message):
        return ""


def set_webhook(secret):
    proxy_url = "http://proxy.server:3128"
    telepot.api._pools = {
        'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
    }
    telepot.api._onetime_pool_spec = (
        urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30)
    )

    bot = telepot.Bot('710918583:AAH6GxWYjn7TRDAcqQ60OBv40T32iUZUwjY')
    bot.setWebhook("https://YOUR_PYTHONANYWHERE_USERNAME.pythonanywhere.com/{}".format(secret), max_connections=1)
