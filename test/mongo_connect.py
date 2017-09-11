from flask import Flask, render_template, make_response
from flask import Flask, request, jsonify, json
from flask import Response

from flask.ext.pymongo import PyMongo

# from sqlalchemy import SQLAlchemy

# from model import User
# from exts import db




app = Flask(__name__)
# app.config.from_object(config)

app.config['MONGO_DBNAME'] = 'connect_to_monogo'
app.config['MONGO_URI'] = 'mongodb://admin:admin@ds115738.mlab.com:15738/mongointernship'

mongo = PyMongo(app)


@app.route('/add')
def add():
    user = mongo.db.users
    user.insert({'name':'joe'})
    return 'added user'

if __name__ == '__main__':
    app.run(debug=True)


