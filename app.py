# import flask and its components
from flask import *

# import pymysql - it helps us create a connection btn python flask and mysql database.
import pymysql

# create a flask application and give it a name.
app = Flask(__name__)





# below is the sign up route.
@app.route("/api/signup", methods=["POST"])
def signup():
    if request.method=="POST":
        # extract the different details entered on the form.
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        phone = request.form["phone"]

        # by use of the print function lets print all those details sent with the upcoming request.
        # print(username,email,password,phone)

        # /establish a connection btn flas and mysql
        connection = pymysql.connect(host="localhost",user="root", password="",database="sokogardenonline")

        # create a cursor to execute the sql queries
        cursor = connection.cursor()

        # structure an sql to insert the details received from the form
        # The percentage s is a place holder- a placeholder stands in places of actual values i.e we shall replace the later on.
        sql = "INSERT INTO users(username,email,phone,password) VALUES(%s,%s,%s,%s)"


        # crete a tuple that will hold all the data gotten from the form.
        data = (username, email, phone, password)

        # by use of the cursor execute the sql as you replace the placeholders with the actual values.

        cursor.execute(sql, data)

        # commit the changes to the  database
        connection.commit()


        return jsonify({"message " : "User registered successfully"})







# run the application.
app.run(debug=True)