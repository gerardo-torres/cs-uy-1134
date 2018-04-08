from flask import Flask
from flask import session
from flask import request
from flask import render_template
from flask.json import jsonify

app = Flask(__name__)
app.secret_key = 'super_duper_secret_key'
app.debug = True


def error(desc):
	return jsonify({
		"error": desc,
		"result" : "failiure"
	})

def success():
	return jsonify({"result": "success"})

@app.route('/todo/create', methods=["POST"]) # 1 - Item Creation
def create():

	if not request.is_json: # check if the request data is in json format
		return error("Requests must be in JSON format")

	if request.cookies.get('session') == None: # check if the sesion cookies are present
		return error("Missing session cookie")

	data = request.json

	if "content" not in data: # check if the todo's title is present
		return error("Missing parameter: 'content'")

	if data["content"] == None or len(data["content"]) == 0: # check if the todo's title has content in it
		return error("Parameter cannot be empty: 'content'")

	if "todos" not in session.keys(): # check if the session variable has been initialized
		session["todos"] = []

	todos = session["todos"]
	todos.append({
		"title": data["content"],
		"done" : False
	})
	session["todos"] = todos
	session.modified = True
	
	return success()


@app.route('/todo/read', methods=["GET"]) # 2 - Fetch List
def fetch():
	if request.cookies.get('session') == None: # check if the sesion cookies are present
		return error("Missing session cookie")
	# if "todos" not in session.keys(): # check if the session variable has been initialized
	# 	session["todos"] = []
	print(session["todos"])
	return jsonify({
			"result" : "success",
			"data" : session["todos"]
		})

@app.route('/todo/update', methods=["PUT"]) # 3 - Item Update
def update():
	if not request.is_json: # check if the request data is in json format
		return error("Requests must be in JSON format")

	if request.cookies.get('session') == None: # check if the sesion cookies are present
		return error("Missing session cookie")

	data = request.json

	if "item_number" not in data: # check if the todo's index is present
		return error("Missing parameter: 'item_number'")

	if data["item_number"] == None: # check if the todo's index has content in it
		return error("Parameter cannot be empty: 'item_number'")

	# having the 'content' parameter is not essential, since the todo cn be updated through its index number

	if "content" not in data: # check if the todo's title is present
		return error("Missing parameter: 'content'")
		
	if data["content"] == None or len(data["content"]) == 0: # check if the todo's title has content in it
	 	return error("Parameter cannot be empty: 'content'")

	index = data["item_number"]
	todos = session["todos"]

	if not (0 <= index < len(todos)):
		return error("Item number out of range")

	todos[index]["done"] = not todos[index]["done"]
	session.pop("todos")
	session["todos"] = todos
	session.modified = True
	print(session["todos"])
	return success()	

@app.route('/todo/delete', methods=["DELETE"]) # 4 - Item Delete
def delete():
	if not request.is_json: # check if the request data is in json format
		return error("Requests must be in JSON format")

	if request.cookies.get('session') == None: # check if the sesion cookies are present
		return error("Missing session cookie")

	data = request.json

	if "item" not in data: # check if the todo's index is present
		return error("Missing parameter: 'item'")

	if data["item"] == None: # check if the todo's index has content in it
		return error("Parameter cannot be empty: 'item'")

	index = data["item"]
	todos = session["todos"]

	if not (0 <= index < len(todos)):
		return error("Item number out of range")

	todos.pop(index)
	session.pop("todos")
	session["todos"] = todos
	session.modified = True

	return success()

@app.route('/',methods=["GET"]) # 5 - Main interface page
def index():
	session.permanent = True;
	if "todos" not in session.keys(): # check if the session variable has been initialized
		session["todos"] = []
	return render_template("index.html")

if __name__ == "__main__":
    app.run()
