import system.command


class StartCommand(system.command.Command):
    def __init__(self):
        super().__init__()
        self.description = ''

    def process(self, text):
        return start(text)


def start(text):
    return 'I am the EK DORN community VK POEbot', ''
