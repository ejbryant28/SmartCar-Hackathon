app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

@app.before_request
def before_request():
	pass

@app.route('/login', methods=["POST"])
def login():
	username = request.form.get('username')
    username = username.lower()

    password = request.form.get('password')

    user = User.query.filter(User.username==username).first()

    return True


@app.route('/login-with-face', methods=["POST"])
def login-face():
	

	return True

@app.route('/upload-potential-item', methods=["POST"])
def upload-potential-item():
	pass

@app.route('/inventroy-by-location' methods=["GET"])
def inventroy-by-location():
	pass

@app.route('/inventory-for-car', methods=["GET"])
def inventory():
	pass











if __name__ == "__main__": #pragma no cover
    app.debug = True
    app.jinja_env.auto_reload = app.debug

    connect_to_db(app, 'postgres:///hackbrighthackathon')

    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    app.run(port=5000, host='0.0.0.0')