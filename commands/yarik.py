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

    address = "https://yandex.ru/search/?"
    region = "lr=2&"
    query_start = "text="
    q = address + region + query_start + "%20".join(query.split())

    html_request = ai_engine.default_answer_seeker.mk_request(q)  # это html запроса в яндексе. используй его с умом. дляя получения другого html по любой другой ссылке - используй тот же метод.

    return str(), ''
