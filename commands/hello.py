import system.command_system


def hello():
    message = 'Привет, друг!\nЯ новый чат-бот.'
    return message, ''


hello_command = system.command_system.Command()

hello_command.key = 'привет'
hello_command.description = 'Поприветствую тебя'
hello_command.process = hello
