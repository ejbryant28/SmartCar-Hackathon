import smartcar
from flask import Flask, request, jsonify
# from flask import (g, Flask, render_template, redirect, request, flash, session, url_for, send_from_directory, jsonify)

CLIENT_ID = 'abf7a59f-c6fa-4225-af72-94531be7fec9'
CLIENT_SECRET = '83e2f996-17b7-4888-a127-ca7f37c6cf9e'

# app = Flask(__name__)

client = smartcar.AuthClient(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri='http://localhost:8000/callback',
    scope=['read_vehicle_info', 'read_location', 'read_odometer']
)

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# @app.before_request
# def before_request():

# @app.route('receive-smart-car')
# def receive_result():



# app = Flask(__name__)

client = smartcar.AuthClient(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri='http://localhost:5000/callback',
    scope=['read_vehicle_info', 'read_location', 'read_odometer']
)

@app.route('/', methods=['GET'])
def index():
    auth_url = client.get_auth_url(force=True)
    return '''
        <h1>Hello, Hackbright!</h1>
        <a href=%s>
          <button>Connect Car</button>
        </a>
    ''' % auth_url

@app.route('/callback', methods=['GET'])
def callback():
    code = request.args.get('code')
    access = client.exchange_code(code)
    
    print(access)

    return jsonify(access)



# @app.route('/login', methods=["POST"])
# def login():
# 	username = request.form.get('username')
#     username = username.lower()

#     password = request.form.get('password')

#     user = User.query.filter(User.username==username).first()

#     result = True
#     return jsonify(result)


# @app.route('/login-with-face', methods=["POST"])
# def login_face():
	
#     result = True
#     return jsonify(result)

@app.route('/upload-potential-item', methods=["POST"])
def upload_potential_item():
	
    result = True
    return jsonify(result)


@app.route('/inventory-by-location', methods=["GET"])
def inventroy_by_location():
	
    result = True
    return jsonify(result)


@app.route('/inventory-for-car', methods=["GET"])
def inventory():
	
    result = True
    return jsonify(result)











if __name__ == "__main__": #pragma no cover
    app.debug = True
    app.jinja_env.auto_reload = app.debug

    # connect_to_db(app, 'postgres:///hackbrighthackathon')

    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    # app.run(port=9090)

    app.run(port=5000, host='10.0.2.15')
