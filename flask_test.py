from flask import request,jsonify
import flask
from dictionary import students

app = flask.Flask(__name__)
app.config['DEBUG']=True

# @app.route('/')
# def signin():
#     return render_template('login.html')
#
# @app.route('/home',methods=["POST"])
# def homep():
#     name = request.form['uname']
#     return render_template('dash.html',name=name)
#
@app.route('/', methods=['GET'])
def signin():
    return '<h1>Hello World</h1>'

@app.route('/students', methods=['GET'])
def api_id():
    if 'Rollno' in request.args:
        id=int(request.args['Rollno'])
    else:
        return '<h1>Wrong id</h1>'
    res=[]
    for student in students:
        if id==student['Rollno']:
            res.append(student)
    return jsonify(res)


app.run()