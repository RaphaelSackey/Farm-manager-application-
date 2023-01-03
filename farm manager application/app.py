import sqlite3
import random
from flask import Flask, session, render_template, request , g, redirect, url_for

app = Flask(__name__)
app.secret_key ="ahkdsfhj_asdhke"
@app.route("/", methods = ["POST", "GET"])
def index():
    session ["all_items"], session ["food_items"] = get_db()
    return render_template("index.html", all_items = session ["all_items"], food_items = session ["food_items"])

@app.route("/add_items", methods= ["post"])
def add_items():
    session ["food_items"].append(request.form["select_food"])
    session.modified = True
    return render_template("index.html", all_items = session ["all_items"], food_items = session ["food_items"])


@app.route("/remove_animal", methods= ["post"])
def remove_animal():
    sold = request.form.getlist("sold")
    for item in sold:
        if item in session["food_items"]:
           index = session["food_items"].index(item)
           session["food_items"].pop(index)
           session.modified = True
    return render_template("index.html", all_items = session ["all_items"], food_items = session ["food_items"])

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('animals.db')
        cursor = db.cursor()
        cursor.execute("select animal_name from animals ")
        all_data = cursor.fetchall()
        all_data = [str (val[0]) for val in all_data]

        animal_list = all_data.copy()
        random.shuffle(animal_list)
        animal_list = animal_list[:6]
    
    return all_data, animal_list

@app.route("/add_to_db", methods = ["POST", "GET"])
def insert():
    name = request.form["Name"]
    number = request.form["number"]
    connection = sqlite3.connect('animals.db')
    cur = connection.cursor()
    query = "INSERT INTO animals Values('{a}',{c})".format(a = name, c = number)
    connection.execute(query)
    connection.commit()
    connection.close()
    return redirect(url_for('index'))
    return render_template("inde.html")

@app.route("/del_from_db", methods = ["POST", "GET"])
def delete():
    name = request.form["DelName"]
    connection = sqlite3.connect('animals.db')
    cur = connection.cursor()
    query = "DELETE FROM animals WHERE animal_name = ?"
    connection.execute(query,(name,))
    connection.commit()
    connection.close()
    return redirect(url_for('index'))
    return render_template("inde.html")



@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__name__':
    app.run(debug=type)

