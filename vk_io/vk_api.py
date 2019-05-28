import vk
import vk_io.settings
import random
import sys

session = vk.Session(vk_io.settings.token)
api = vk.API(session, v=5.95)


def send_message(user_id, token, message, attachment=""):
    api.messages.send(access_token=token, random_id=random.randint(0, sys.maxsize), user_id=str(user_id), message=message, attachment=attachment)
