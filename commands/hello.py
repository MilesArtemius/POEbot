import system.command


class HelloCommand(system.command.Command):
    def __init__(self):
        super().__init__()
        self.description = 'Поприветствую тебя'

    def process(self, text):
        return hello(text)


def hello(text):
    message = 'Привет, друг!\nЯ новый чат-бот.'
    return message, ''


description = 'Поприветствую тебя'
process = hello
