import vk_io.vk_api
import os
import importlib
import system.command_system


def load_modules():
    # путь от рабочей директории, ее можно изменить в настройках приложения
    files = os.listdir("vkbot/commands")
    modules = filter(lambda x: x.endswith('.py'), files)
    for m in modules:
        importlib.import_module("commands." + m[0:-3])


def get_answer(body):
    # Сообщение по умолчанию если распознать не удастся
    message = "Прости, не понимаю тебя. Напиши 'помощь', чтобы узнать мои команды"
    attachment = ''
    for c in system.command_system.command_list:
        if body in c.keys:
            message, attachment = c.process()
    return message, attachment


def create_answer(data, token):
    load_modules()
    user_id = data['user_id']
    message, attachment = get_answer(data['body'].lower())
    vk_io.vk_api.send_message(user_id, token, message, attachment)
