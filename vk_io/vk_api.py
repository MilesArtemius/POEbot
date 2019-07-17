import vk
import vk_io.settings
import random
import sys
import system.api


class VkApi(system.api.Api):
    def __init__(self):
        super().__init__()
        self.session = vk.Session(vk_io.settings.token)
        self.api = vk.API(self.session, v=5.95)

    def get_user_id(self, message):
        return message['object']['peer_id']

    def send_message(self, message, user_id, attachment=''):
        self.api.messages.send(access_token=vk_io.settings.token, peer_id=str(user_id), random_id=random.randint(0, sys.maxsize), message=message, attachment=attachment)

    def get_message_text(self, message):
        return message['object']['text']

    def answerable(self, message):
        return message['object']['from_id'] > 0
