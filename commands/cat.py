import system.command_system
import vk_io.vk_api


def cat():
    # Получаем случайную картинку из паблика
    attachment = vk_io.vk_api.get_random_wall_picture(-32015300)
    message = 'Вот тебе котик :)\nВ следующий раз я пришлю другого котика.'
    return message, attachment


cat_command = system.command_system.Command()

cat_command.keys = ['котик', 'кошка', 'кот', 'котенок', 'котяра', 'cat']
cat_command.description = 'Пришлю картинку с котиком'
cat_command.process = cat
