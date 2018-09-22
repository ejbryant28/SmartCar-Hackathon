CLIENT_ID = 'abf7a59f-c6fa-4225-af72-94531be7fec9'
CLIENT_SECRET = '83e2f996-17b7-4888-a127-ca7f37c6cf9e'

app = Flask(__name__)

client = smartcar.AuthClient(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri='http://localhost:8000/callback',
    scope=['read_vehicle_info', 'read_location', 'read_odometer']
)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# @app.before_request
# def before_request():

# @app.route('receive-smart-car')
# def receive_result():


@app.route('/login', methods=["POST"])
def login():
	username = request.form.get('username')
    username = username.lower()

    password = request.form.get('password')

    user = User.query.filter(User.username==username).first()

    result = True
    return jsonify(result)


@app.route('/login-with-face', methods=["POST"])
def login-face():
	
    result = True
    return jsonify(result)

@app.route('/upload-potential-item', methods=["POST"])
def upload-potential-item():
	
    result = True
    return jsonify(result)


@app.route('/inventory-by-location' methods=["GET"])
def inventroy-by-location():
	
    result = True
    return jsonify(result)


@app.route('/inventory-for-car', methods=["GET"])
def inventory():
	
    result = True
    return jsonify(result)











if __name__ == "__main__": #pragma no cover
    app.debug = True
    app.jinja_env.auto_reload = app.debug

    connect_to_db(app, 'postgres:///hackbrighthackathon')

    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    app.run(port=5000, host='0.0.0.0')