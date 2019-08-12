from flask import request,jsonify
import flask
import urllib3
from bs4 import BeautifulSoup
# from dictionary import students

app = flask.Flask(__name__)
app.config['DEBUG']=True

@app.route('/')
def signin():
    return flask.render_template('login.html')

@app.route('/home',methods=["POST"])
def homep():
    name = request.form['uname']
    http = urllib3.PoolManager()
    user = name
    link = "https://github.com/" + user + "?tab=repositories"
    page = http.request('GET', link)
    soup = BeautifulSoup(page.data,"html.parser")
    head = soup.find('div', attrs={'id': 'user-repositories-list'})
    if head==None:
        head = '<h1>User does not exists... :(</h1>'
    # head=head.text.strip()
    # print(scrap)
    return flask.render_template('dash.html',html_data=head)

# @app.route('/', methods=['GET'])
# def signin():
#     return '<h1>Hello World</h1>'

# @app.route('/students', methods=['GET'])
# def api_id():
#     if 'Rollno' in request.args:
#         id=int(request.args['Rollno'])
#     else:
#         return '<h1>Wrong id</h1>'
#     res=[]
#     for student in students:
#         if id==student['Rollno']:
#             res.append(student)
#     return jsonify(res)


app.run()