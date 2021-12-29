from flask import Flask, jsonify, request
from flask_cors import CORS
from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
import pymongo
from pymongo import mongo_client

connection_url = 'mongodb+srv://admin:pass@cluster0.1wcsc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
app = Flask(__name__)
client = pymongo.MongoClient(connection_url)
  
# Database
Database = client.get_database('Example')
# Table
SampleTable = Database.SampleTable

@app.route('/')
def indexx():
    

    return render_template('login.html')



@app.route('/login', methods=['POST'])
def login():
    value=request.form['username']
   

    queryObject = {"username": value}
    query = SampleTable.find_one(queryObject)
    if query:
        if request.form['pass']==query['password']:
            
            return "user is logged"
    return 'Invalid username/password combination'        

@app.route('/register')
def index():
      

    return render_template('register.html')

@app.route('/register' , methods=['POST'])
def indexs():
    value=request.form['username']  

    queryObject = {"username": value}
    query = SampleTable.find_one(queryObject)
    if query is None:
        password=request.form['pass']
        queryObject = {
        'username': value,
        'password': password
        }
        query = SampleTable.insert_one(queryObject)
        return "logged"
        
    return 'That username already exists!'

if __name__ == '__main__':
    app.run(debug=True)    


    


   
