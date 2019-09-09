import datetime
from flask import Flask, render_template, request, flash, redirect, url_for, json, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
import csv
# from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crimedata.sqlite3'
app.config['SECRET_KEY'] = '12132434'
db = SQLAlchemy(app)
# ma = Marshmallow(app)


class Crime(db.Model):
    sn = db.Column('sn', db.Integer, primary_key = True)
    date_occr = db.Column(db.Date)
    date_rep = db.Column(db.Date)
    time_occr = db.Column(db.Time)
    crime_type = db.Column(db.String(100))
    loc = db.Column(db.String(100))
    loc_long = db.Column(db.String(100))
    loc_lat = db.Column(db.String(100))

def __init__(self, sn, date_occr, date_rep, time_occr, crime_type, loc, loc_long, loc_lat):
    self.sn = sn
    self.date_occr = date_occr
    self.date_rep = date_rep
    self.time_occr = time_occr
    self.crime_type = crime_type
    self.loc = loc
    self.loc_long = loc_long
    self.loc_lat = loc_lat


# class CrimeSchema(ma.Schema):
#     class Meta:
#         # Fields to expose
#         fields = ("sn", "date_occurred")

db.create_all()
#
# student = students(name='khadga', city='urlabaari', addr='alskl', pin=1234)
# db.session.add(student)
# db.session.commit()


@app.route("/")
def main():
    crime_by_type = db.session.query(Crime.crime_type, func.count(Crime.sn)).group_by(Crime.crime_type).all()
    return render_template('index.html', crime_by_type=crime_by_type)


@app.route('/showall')
def show_all():
    crime_data = Crime.query.all()
    return render_template('show_all.html', crime_res=crime_data)


@app.route('/crime_by_type')
def crime_by_type():
    crime_by_type = db.session.query(Crime.crime_type, func.count(Crime.sn)).group_by(Crime.crime_type).all()
    return render_template('crime_by_type.html', crime_by_type=crime_by_type)


@app.route('/crime_by_year')
def crime_by_year():
    crime_year = db.session.query(func.extract('year', Crime.date_occr), func.count(func.extract('year', Crime.date_occr)))\
        .group_by(func.extract('year', Crime.date_occr)).all()

    return render_template('crime_rate_year.html', crime_rate=crime_year)


@app.route('/api/coordinates')
def coordinates():
    addresses = db.session.query(Crime.crime_type, Crime.loc, Crime.loc_long, Crime.loc_lat).all()
    all_coords = [] # initialize a list to store your addresses
    for add in addresses:
        address_details = {
        "lat": add.loc_lat,
        "lng": add.loc_long,
        "title": add.loc}
        all_coords.append(address_details)
    return jsonify({'coordinates': all_coords})

@app.route('/crime_map')
def crime_map():
    return render_template('crime_map.html')


# @app.route('/populate')
# def populate():
#     with open('crime_data.csv', 'r') as f:
#         reader = csv.reader(f)
#         your_list = list(reader)
#         for rows in your_list:
#             year1, month1, day1 = map(int, rows[0].split('-'))
#             date1 = datetime.date(year1, month1, day1)
#             year2, month2, day2 = map(int, rows[1].split('-'))
#             date2 = datetime.date(year2, month2, day2)
#             hh, mm = map(int, rows[2].split(':'))
#             time1 = datetime.time(hh, mm, 00)
#             res = Crime(date_occr=date1, date_rep=date2, time_occr=time1, crime_type=rows[3],
#                         loc=rows[4], loc_long=rows[5],
#                         loc_lat=rows[6])
#
#             db.session.add(res)
#             db.session.commit()
#
#     return "hello"

@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['date_occurred'] or not request.form['date_reported'] or not request.form['time_occurred'] or not request.form['crime_type'] or not request.form['crime_loc'] or not request.form['crime_loc_long'] or not request.form['crime_loc_lat']:
            flash('Please enter all the fields', 'error')
        else:
            year1, month1, day1 = map(int, request.form['date_occurred'].split('-'))
            date1 = datetime.date(year1, month1, day1)
            year2, month2, day2 = map(int, request.form['date_reported'].split('-'))
            date2 = datetime.date(year2, month2, day2)
            hh, mm = map(int, request.form['time_occurred'].split(':'))
            time1 = datetime.time(hh,mm,00)
            res = Crime(date_occr=date1, date_rep=date2,time_occr=time1, crime_type=request.form['crime_type'], loc=request.form['crime_loc'], loc_long=request.form['crime_loc_long'], loc_lat=request.form['crime_loc_lat'])

            db.session.add(res)
            db.session.commit()

            flash('Record was successfully added')
        return redirect(url_for('show_all'))
    return render_template('add_new.html')


# crimeSchema=CrimeSchema()



@app.route('/get-data')
def get_data():

    #crime_data = Crime.query.all()
    # crime_res = {}
    # i = 0
    # for crime in crime_data:
    #     crime_res =

     with open('crime_data.csv', 'r') as f:
        reader = csv.reader(f)
        your_list = list(reader)

     return Response(json.dumps(your_list), mimetype='application/json')

    # crimes=crimeSchema.dump(crime_data);
    # return jsonify({'data':crimes})


if __name__ == "__main__":
    app.run(debug='true')
