from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
	"""Users."""

	__tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    contributor = db.Column(db.Boolean, nullable=True)
    consumer = db.Column(db.Boolean, nullable=True)
    username = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(256), nullable=False, unique=True)
    email = db.Column(db.String(128), nullable=False, unique=True)


class Car(db.Model):
	"""Cars."""

	__tablename__ = "cars"

	car_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	location = db.Column(db.String(256), nullable=False)
	locked = db.Column(db.Boolean, nullable=False)


class Category(db.Model):
	"""Categories."""

	__tablename__ = "categories"

	category = db.Column(db.String(64), primary_key=True)


class Donatable(db.Model):
	"""Donatables."""

	__tablename__ = "donatables"

	name = db.Column(db.String(64), primary_key=True)


class Items(db.Model):
	"""Items."""

	__tablename__ = "items"

	item_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	name = db.Columnn(db.String(64), db.ForeignKey('donatables.donatable'))
	category = db.Column(db.String(64), db.ForeignKey('categories.category'), nullable=False)
	car_id = db.Column(db.Integer, db.ForeignKey('cars.car_id'))
	donator_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
	consumer_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=True)
	date_given = db.Column(db.DateTime, nullable=False)
	date_taken = db.Column(db.DateTime, nullable=True)


	item = db.relationship('Donatable')
	car = db.relationship('Car')
	donator = db.relationship('User')
	consumer = db.relationship('User')




##############################################################################
def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":

    from server import app
    connect_to_db(app)
    db.create_all()
    print "Connected to DB."



