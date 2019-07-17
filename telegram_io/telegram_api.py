import telepot
import urllib3
import system.api
import telegram_io.settings


class TelegramApi(system.api.Api):
    def __init__(self):
        super().__init__()
        self.bot = telepot.Bot(telegram_io.settings.token)

    def get_user_id(self, message):
        return message['message']['from']['id']

    def send_message(self, message, user_id, attachment, token):
        self.bot.sendMessage(self.get_user_id(message), 'Hey!').wait()

    def get_message_text(self, message):
        return message['message']['text']


def set_webhook(secret):
    telepot.api._pools = {
        'default': urllib3.ProxyManager(proxy_url=telegram_io.settings.proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
    }
    telepot.api._onetime_pool_spec = (
        urllib3.ProxyManager, dict(proxy_url=telegram_io.settings.proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30)
    )

    bot = telepot.Bot(telegram_io.settings.token)
    bot.setWebhook("https://milty.pythonanywhere.com/{}".format(secret), max_connections=1)
