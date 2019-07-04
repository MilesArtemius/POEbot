import os

import flask
import vk_io.settings
import system.main_handler
import git
import telegram_io.telegram_api

secret = ""
app = flask.Flask(__name__)
telegram_io.telegram_api.set_webhook(secret)


@app.route('/{}'.format(secret), methods=['POST'])
def processing():
    data = flask.json.loads(flask.request.data)
    # revise & remove vk dependency
    system.main_handler.load_api()
    if 'message' in data.keys():
        f = open(os.path.join(os.getcwd(), 'tlg_msg.txt'), "w+")
        f.write(str(data))
        f.flush()
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return vk_io.settings.confirmation_token
    elif data['type'] == 'message_new':
        f = open(os.path.join(os.getcwd(), 'vk_msg.txt'), "w+")
        f.write(str(data))
        f.flush()
        system.main_handler.build(data['object'])
        return 'ok'
    return '', 200


@app.route('/{}_webhook'.format(secret), methods=['POST'])
def webhook():
    repo = git.Repo('/home/milty/POEbot')
    origin = repo.remotes.origin
    repo.create_head('master', origin.refs.master).set_tracking_branch(origin.refs.master).checkout()
    origin.pull()
    return '', 200
