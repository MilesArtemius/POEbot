import system.command
import ai_engine.default_answer_seeker


class StartCommand(system.command.Command):
    def __init__(self):
        super().__init__()
        self.description = 'bochok potik :/'

    def process(self, text):
        return search(text)


def search(text):
    if len(text) > 0:
        query = text[0]
    else:
        query = 'pneis'

    html_request = ai_engine.default_answer_seeker.mk_request_in_yandex(query)  # это html запроса в яндексе. используй его с умом. дляя получения другого html по любой другой ссылке - используй метод mk_request.

    return str(), ''
