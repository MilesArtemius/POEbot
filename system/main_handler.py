import importlib
import inspect
import os

import console_io.console_api
import system.command
import telegram_io.telegram_api
import vk_io.vk_api

api = console_io.console_api.ConsoleApi()


# 0 is for console io, 1 - for vk, 2 - for telegram
def load_api(marker, string):
    global api
    if marker == 1:
        f = open(os.path.join(os.getcwd(), 'vk_messages.txt'), "a")
        f.write(string['object']['text'])
        f.write('\n')
        f.write('--- ' + str(string['object']['peer_id']))
        f.write('\n\n\n')
        f.flush()
        api = vk_io.vk_api.VkApi()
    elif marker == 2:
        api = telegram_io.telegram_api.TelegramApi()


def get_answer(text):
    message, attachment = '', ''
    if text[0][0] == '/':
        try:
            module = importlib.import_module('commands.' + text[0][1:])
            inst = system.command.Command()

            for name, obj in inspect.getmembers(module):
                if inspect.isclass(obj) and issubclass(obj, system.command.Command):
                    inst = obj()
                    break

            message, attachment = inst.process(text[1:])
        except ModuleNotFoundError:
            message = "There is no such command!"
    else:
        message = ""
        # chat with user
    return message, attachment


def build(data):
    message, attachment = get_answer(api.get_message_text(data).split())
    if message != "":
        api.send_message(message, api.get_user_id(data), attachment)
