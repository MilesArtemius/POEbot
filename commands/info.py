import importlib
import inspect
import os
import system.command


class InfoCommand(system.command.Command):
    def __init__(self):
        super().__init__()
        self.description = 'Покажу список команд'

    def process(self, text):
        return info(text)


def info(text):
    message = ''
    files = os.listdir(os.path.join(os.getcwd(), "commands"))
    modules = filter(lambda x: not x.startswith('__') and x.endswith('.py'), files)
    for m in modules:
        mod = importlib.import_module("commands." + m[0:-3])
        inst = system.command.Command()

        for name, obj in inspect.getmembers(mod):
            if inspect.isclass(obj) and issubclass(obj, system.command.Command):
                inst = obj()
                break
        message += '/' + m[0:-3] + ' - ' + inst.description + '\n'

    return message, ''
