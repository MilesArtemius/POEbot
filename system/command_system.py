command_list = []


class Command:
    def __init__(self):
        self.__key = ''
        self.description = ''
        command_list.append(self)

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, mas):
        self.__key = mas.lower()

    def process(self):
        pass
