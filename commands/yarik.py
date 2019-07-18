import system.command
import ai_engine.default_answer_seeker


class StartCommand(system.command.Command):
    def __init__(self):
        super().__init__()
        self.description = 'bochok potik :/'

    def process(self, text):
        return start(text)


def start(text):
    if len(text) > 0:
        query = text[0]
    else:
        query = 'pneis'
    return str(ai_engine.default_answer_seeker.mk_request(query)), ''
