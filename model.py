from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
	"""Users."""

	__tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    contributor = db.Column(db.Boolean, nullable=True)
    consumer = db.Column(db.Boolean, nullable=True)
    username = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(64), nullable=False, unique=True)
    email = db.Column(db.String(64), nullable=False, unique=True)


class Cars(db.Model):
	"""Cars."""

	__tablename__ = "cars"

	car_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	# location = 
	locked = db.Column(db.Boolean, nullable=False)


class Items(db.Model):
	"""Items."""

	__tablename__ = "items"

	item_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	category = db.Column(db.String(64), nullable=False)
	car_id = db.Column(db.Integer, db.ForeignKey('cars.car_id'))