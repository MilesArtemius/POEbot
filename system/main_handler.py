import importlib
import inspect

import console_io.console_api
import system.command
import vk_io.vk_api

api = console_io.console_api.ConsoleApi()


def load_api():
    global api
    # loading default vk api
    api = vk_io.vk_api.VkApi()


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
        message = "lol"
        # chat with user
    return message, attachment


def build(data):
    message, attachment = get_answer(api.get_message_text(data).split())
    if message != "":
        api.send_message(message, api.get_user_id(data), attachment)
