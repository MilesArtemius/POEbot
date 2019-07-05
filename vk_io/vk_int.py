import vk_api
import vk_io.settings
import random
import sys
import system.api


class VkApi(system.api.Api):
    def __init__(self):
        super().__init__()
        self.vk = vk_api.VkApi(token=vk_io.settings.token)
        self.vk_api = self.vk.get_api()

    def get_user_id(self, message):
        peer_id = message['object']['from_id']
        if peer_id < 2000000000:
            return peer_id
        else:
            return peer_id - 2000000000

    def send_message(self, message, user_id, attachment='', token=vk_io.settings.token):
        self.vk_api.messages.send(peer_id=user_id, message=message)

    def get_message_text(self, message):
        return message['object']['text']
