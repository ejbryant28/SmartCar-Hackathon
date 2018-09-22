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

    if user is None:

    	flash("Ooops. Try entering again.")
        return redirect('/login')

    elif user.password == password:
    	flash("You're logged in")
    	return redirect('/login')

    else:
    	flash("Password doesn't match. Try again")
    	return redirect('/upload-potential-item')


@app.route('/login-with-face', methods=["POST"])
def login-face():
	pass

@app.route('/upload-potential-item', methods=["POST"])
def upload-potential-item():
	pass

@app.route('/inventory', methods=["GET"])
def inventory():
	pass











if __name__ == "__main__": #pragma no cover
    app.debug = True
    app.jinja_env.auto_reload = app.debug

    connect_to_db(app, 'postgres:///hackbrighthackathon')

    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    app.run(port=5000, host='0.0.0.0')