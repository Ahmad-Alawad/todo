from flask import Flask, render_template, request, flash, redirect, session
from model import User, Item, db

app = Flask(__name__)


app.secret_key = "ABC"


@app.route('/')
def index():
    """Homepage."""

    users = User.query.all()
    return render_template("mainpage.html", users=users)


@app.route('/add_user')
def add_user():
	return render_template('addUser.html')



@app.route('/process_add_user', methods=['POST'])
def process_add_user():

	display_name = request.form["display_name"]
	new_user = User(display_name=display_name)
	
	db.session.add(new_user)
	db.session.commit()

	flash("User %s added." % display_name, "info")
	return redirect("/")



@app.route('/user/<int:user_id>')
def display_user_info(user_id):

	user = User.query.get(user_id)
	
	session['current_user'] = user_id

	todo_items = Item.query.filter(Item.user_id==user_id).all()


	return render_template("user_info.html", user=user, todo_items=todo_items)



@app.route('/add_item')
def add_items():
	return render_template("add_item.html")


@app.route('/process_add_item', methods=['POST'])
def process_add_items():

	item = request.form["item"]
	user_id = session["current_user"]
	new_item = Item(item_name = item, user_id=user_id)
	db.session.add(new_item)
	db.session.commit()

	# flash("User %s added." % display_name, "info")

	return redirect('/user/'+str(user_id))




if __name__ == "__main__":
	from model import connect_to_db
	connect_to_db(app)

	app.run(port=5002, host='0.0.0.0')