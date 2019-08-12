import datetime
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crimedata.sqlite3'
app.config['SECRET_KEY'] = '12132434'
db = SQLAlchemy(app)


class crimedata(db.Model):
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

# db.create_all()
#
# student = students(name='khadga', city='urlabaari', addr='alskl', pin=1234)
# db.session.add(student)
# db.session.commit()


@app.route("/")
def main():
    return render_template('index.html')


@app.route('/showall')
def show_all():
    crime_data = crimedata.query.all()
    return render_template('show_all.html', crime_res=crime_data)


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
            res = crimedata(date_occr=date1, date_rep=date2,time_occr=time1, crime_type=request.form['crime_type'], loc=request.form['crime_loc'], loc_long=request.form['crime_loc_long'], loc_lat=request.form['crime_loc_lat'])

            db.session.add(res)
            db.session.commit()

            flash('Record was successfully added')
        return redirect(url_for('show_all'))
    return render_template('add_new.html')


if __name__ == "__main__":
    app.run()
