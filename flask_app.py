import flask
import vk_io.settings
import system.main_handler
import git
import telegram_io.telegram_api

secret = ""
app = flask.Flask(__name__)
#telegram_io.telegram_api.set_webhook(secret)


@app.route('/{}'.format(secret), methods=['POST'])
def processing():
    data = flask.json.loads(flask.request.data)
    system.main_handler.load_api(check_source(data))
    if data['type'] == 'confirmation':
        return vk_io.settings.confirmation_token
    else:
        system.main_handler.build(data)
        return 'ok'


@app.route('/{}_webhook'.format(secret), methods=['POST'])
def webhook():
    repo = git.Repo('/home/milty/POEbot')
    origin = repo.remotes.origin
    repo.create_head('master', origin.refs.master).set_tracking_branch(origin.refs.master).checkout()
    origin.pull()
    return '', 200


def check_source(message):
    if message['object'] in message.keys():
        return 1
    elif message['message'] in message.keys():
        return 2
    else:
        return 0
