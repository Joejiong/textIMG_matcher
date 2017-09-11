from flask import Flask, render_template, make_response
from flask import Flask, request, jsonify, json
from flask import Response
from flask.ext.sqlalchemy import SQLAlchemy
import config
from flask.ext.pymongo import PyMongo

# from sqlalchemy import SQLAlchemy

# from model import User
# from exts import db




app = Flask(__name__)
app.config.from_object(config)

# app.config['MONGO_DBNAME'] = 'connect_to_monogo'
# app.config['MONGO_URI'] = 'mongodb://videosense:cf789465@ds115738.mlab.com:15738/mongointernship'

# mongo = PyMongo(app)
#
# @app.routr('/add')
# def add():
#     user = mongo.db.users
#     user.insert({'name':'joe'})
#     return 'added user'
# db.init_app(app)


db = SQLAlchemy(app)
print(db)

po = {'number':89,'name':"haha"}

db.create_all()


pokedex = [
    {'number': 14, 'name': 'Kakuna'},
    {'number': 16, 'name': 'Pidgey'},
    {'number': 50, 'name': 'Diglett'},
    ]


@app.route("/")
def main():
    return render_template('QA.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)


def valid_login(username,password):
    if username == 'admin' and password == 'admin':
        return True
    else:
        return False


def log_the_user_in(username):
    resp = make_response(render_template('index.html', username = username))
    resp.set_cookie('username', username)
    return resp



# @app.route('/login', methods=['GET'])

# def login():
#     return render_template('login.html')


# @app.route('/login/<username>/', methods=['POST'])
# def login():
#     return render_template('login.html')



@app.route("/regist/",methods=['GET','POST'])
def regist():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        telephone = request.form.get('telephone')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # if already regist cannot regist
        # user = User.query.filter(User.telephone == telephone).first()
        # if user:
        #   return 'this phone is already regist'
        # else:
        #   user = User(telephone=telephone,username=username,password=password1)
        #   return render_template('index.html')

@app.route("/jsTest")
def jsTest():
    return render_template('jsclient.html')


@app.route("/content")
def content():
    return render_template('content.html')


# @app.route("/content/<username>")
# def content(username):
#     return render_template('content.html', username=username)


@app.route('/hello/<username>', methods=['POST', 'GET'])
def hello(username):
    return 'User %s' % username


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/api/v1/pokemon', methods=('GET', 'POST'))
def pokemon():
    if request.method == 'GET':
        response = pokedex
        return Response(json.dumps(response), mimetype='application/json')


    else:  # POST
        if request.content_type != 'application/json':
             return jsonify({})
        try:
            new_pokemon = json.loads(request.data)
            print(new_pokemon['text'][:4])
            return Response(json.dumps(new_pokemon), mimetype='application/json')
        except ValueError as err:
            return jsonify(err)

        # if 'number' in new_pokemon and isinstance(new_pokemon['number'], int) and \
        #    'name' in new_pokemon and isinstance(new_pokemon['name'], str) and \
        #    len(new_pokemon.keys()) == 2 and new_pokemon not in pokedex:
        #     pokedex.append(new_pokemon)
        #     response = pokedex[-1]
    # else:





if __name__ == "__main__":
    app.run(debug=True)
