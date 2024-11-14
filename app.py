from flask import Flask, jsonify, request, render_template
from flask_mysqldb import MySQL
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# MySQL Config
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DB'] = 'bookstore'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

#Add A new Function
def add_book():
    data = request.json
    title = data['title']
    author = data['author']
    isbn = data['isbn']


    if not title:
        return {"error": "Title is required"}, 400
    if not author:
        return {"error": "Author is required"}, 400
    if not isbn:
        return {"error": "ISBN is required"}, 400

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO books (title, author, isbn) VALUES (%s, %s, %s)", (title, author, isbn))
    mysql.connection.commit()
    cur.close()
    

if __name__ == '__main__':
    app.run(debug=True)