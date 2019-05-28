import flask
import vk_io.settings
import system.message_handler
import vk
import git

app = flask.Flask(__name__)


@app.route('/')
def processing():
    if flask.request.method == 'POST':
        data = flask.json.loads(flask.request.data)
        if 'type' not in data.keys():
            return 'not vk'
        if data['type'] == 'confirmation':
            return vk_io.settings.confirmation_token
        elif data['type'] == 'message_new':
            session = vk.Session()
            api = vk.API(session, v=5.0)
            user_id = data['object']['user_id']
            api.messages.send(access_token=vk_io.settings.token, user_id=str(user_id), message='Привет, я новый бот!')
            #system.message_handler.create_answer(data['object'], vk_io.settings.token)
            return 'ok'
    else:
        return 'Bot\'s heart beating'


@app.route('/webhook', methods=['POST'])
def webhook():
    repo = git.Repo('/home/milty/POEbot')
    origin = repo.remotes.origin
    repo.create_head('master', origin.refs.master).set_tracking_branch(origin.refs.master).checkout()
    origin.pull()
    return '', 200
