from flask import Flask, render_template, redirect, request
from mysqlconnection import MySQLConnection, connectToMySQL # import the function that will return an instance of a connection
app = Flask(__name__)

@app.route('/dojos')
def index():
    mysql = connectToMySQL('dojos_and_ninjas_schema')
    dojos = mysql.query_db('SELECT * FROM dojo;') 
    return render_template('index.html', all_dojos = dojos)

@app.route("/create", methods=["POST"])
def create_():
    mysql= connectToMySQL('dojos_and_ninjas_schema')
    query = 'INSERT INTO dojo (name, created_at, updated_at) VALUES (%(nam)s, NOW(), NOW())'
    data = {
        "nam" : request.form ["name_of_loc"]
    }
    mysql.query_db(query,data)
    return redirect('/dojos')


@app.route("/ninjas")
def new_ninja():
    mysql= connectToMySQL('dojos_and_ninjas_schema')
    dojos = mysql.query_db('SELECT * FROM dojo;')
    return render_template("new_ninja.html", all_dojos = dojos)



@app.route("/createninja", methods = ["POST"])
def create_ninja():
    mysql= connectToMySQL('dojos_and_ninjas_schema')
    query = 'INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at) VALUES (%(fn)s, %(ln)s, %(ag)s, %(djid)s, NOW(), NOW());'
    data = {
        "fn" : request.form["fname"],
        "ln" : request.form["lname"],
        "ag" : request.form["age"],
        "djid" : request.form["dojo_id"]
    }
    mysql.query_db(query,data)
    return redirect('/dojos')


@app.route("/dojos/<id>")
def show(id):
    mysql = connectToMySQL('dojos_and_ninjas_schema')
    mysql2 = connectToMySQL('dojos_and_ninjas_schema')
    query = 'SELECT * FROM ninjas WHERE dojo_id=%(id)s;'
    query2= 'SELECT * FROM dojo WHERE id = %(id)s'
    data = {
        "id" : int(id)
    }
    dojos = mysql.query_db(query, data)
    dojo = mysql2.query_db(query2,data)
    print(dojo)
    return render_template("show_ninja.html", all_dojos = dojos, dojo = dojo[0])













if __name__ == "__main__":
    app.run(debug=True)