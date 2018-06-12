from flask import Flask, render_template, request, url_for, session, flash, jsonify, redirect
from flaskext.mysql import MySQL
import hashlib, uuid

app = Flask(__name__)

mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'injung'
app.config['MYSQL_DATABASE_DB'] = 'FlaskDB'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()

#Main Page
@app.route("/")
def home():
    return render_template('index.html', **locals())

#The post for creating a new user
@app.route("/signup", methods=['POST'])
def signup():
    username = request.form['signup-username']
    password = request.form['signup-password']
    password_confirm = request.form['signup-password-confirm']

    #Check that none of the fields are empty
    if not username or not password:
        return jsonify({"Error" : "Username or password was null."}), 405
    
    #Check that password and password_confirm match
    if password_confirm != password:
        return jsonify({"Error" : "Passwords did not match."}), 401

    #Hash and salt password for storage
    password = hashlib.sha512((password + username).encode('utf-8')).hexdigest()

    #Calls the stored SQL procedure for creating a user
    cursor.callproc('signup',(username,password))
    data = cursor.fetchall()
 
    #If the procedure return is empty, procedure was successful. Otherwise there was an error.
    if len(data) is 0:
        return jsonify({"error" : data[0][0]}), 402
    else:
        conn.commit()
        return jsonify({"success" : "User created successfully!"}), 200
        #return render_template('index.html', **locals())



#The post for logging in as an existing user
@app.route("/login", methods=['GET', 'POST'])
def login():
    username = request.form['login-username']
    password = request.form['login-password']

    #hash and salt the password for table lookup
    password = hashlib.sha512((password + username).encode('utf-8')).hexdigest()

    #calls the stored SQL procedure for looking up a user
    cursor.callproc('login',(username,password))
    data = cursor.fetchall()
 
    #if the database return is empty, no user was found. Otherwise login was successful
    if len(data) is 0:
        return jsonify({"error" : "Username or password was incorrect."}), 400

    else:
        conn.commit()        
        return jsonify({"success" : "User logged in successfully!", "user_id" : data[0][0], "session_key" : data[0][1], "timestamp" : data[0][2]}), 200
        #return redirect(url_for('photo'))
    
@app.route('/photo')
def photo():
    return redirect("http://0.0.0.0:3000")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

    
