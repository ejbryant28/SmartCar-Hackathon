app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"










if __name__ == "__main__": #pragma no cover
    app.debug = True
    app.jinja_env.auto_reload = app.debug

    connect_to_db(app, 'postgres:///hackbrighthackathon')

    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    app.run(port=5000, host='0.0.0.0')