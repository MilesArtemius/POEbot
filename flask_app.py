import flask
import vk_io.settings
import system.message_handler
import git

app = flask.Flask(__name__)


@app.route('/', methods=['POST'])
def processing():
    data = flask.json.loads(flask.request.data)
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return vk_io.settings.confirmation_token
    elif data['type'] == 'message_new':
        system.message_handler.create_answer(data['object'], vk_io.settings.token)
        return 'ok'
    return '', 200


@app.route('/webhook', methods=['POST'])
def webhook():
    repo = git.Repo('/home/milty/POEbot')
    origin = repo.remotes.origin
    repo.create_head('master', origin.refs.master).set_tracking_branch(origin.refs.master).checkout()
    origin.pull()
    return '', 200
