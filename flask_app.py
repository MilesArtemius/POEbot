import flask
import vk_io.settings
from system import main_handler
import git

app = flask.Flask(__name__)


@app.route('/', methods=['POST'])
def processing():
    data = flask.json.loads(flask.request.data)
    # revise & remove vk dependency
    main_handler.load_api()
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return vk_io.settings.confirmation_token
    elif data['type'] == 'message_new':
        main_handler.build(data['object'])
        return 'ok'
    return '', 200


@app.route('/webhook', methods=['POST'])
def webhook():
    repo = git.Repo('/home/milty/POEbot')
    origin = repo.remotes.origin
    repo.create_head('master', origin.refs.master).set_tracking_branch(origin.refs.master).checkout()
    origin.pull()
    return '', 200
