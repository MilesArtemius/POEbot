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
        peer_id = message['object']['peer_id']
        if peer_id < 2000000000:
            return peer_id
        else:
            return peer_id - 2000000000

    def send_message(self, message, user_id, attachment='', token=vk_io.settings.token):
        self.api.messages.send(access_token=token, random_id=random.randint(0, sys.maxsize), user_id=str(user_id), message=message, attachment=attachment)

    def get_message_text(self, message):
        return message['object']['text']
