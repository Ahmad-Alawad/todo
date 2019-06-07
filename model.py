from flask_sqlalchemy import SQLAlchemy

# from server import app

db = SQLAlchemy()


class User(db.Model):

	"""
		User will have many items in the todo list
	"""

	__tablename__ = "users"

	user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)

	display_name = db.Column(db.String(64))

	items = db.relationship("Item",
								backref=db.backref("items", order_by=user_id))


class Item(db.Model):

	"""
		Items will be added uniquely for a specific user's todo list
	"""

	__tablename__ = "items"

	item_id = db.Column(db.Integer, autoincrement=True, primary_key=True)

	item_name = db.Column(db.String(64))

	user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

	

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///todo'
    db.app = app
    db.init_app(app)
    db.create_all()
    db.session.commit()