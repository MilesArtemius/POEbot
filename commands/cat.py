import system.command


class CatCommand(system.command.Command):
    def __init__(self):
        super().__init__()
        self.description = 'Fuck you!'

    def process(self, text):
        return cat(text)


def cat(text):
    return 'fuck da life', ''
