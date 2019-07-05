import system.api


class ConsoleApi(system.api.Api):
    def get_user_id(self, message):
        return 'user'

    def send_message(self, message, user_id='', attachment='', token=''):
        print(message)

    def get_message_text(self, message):
        return message['text']
