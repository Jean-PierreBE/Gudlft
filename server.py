"""
    main programm
"""
from flask import Flask, render_template, request, redirect, flash, url_for
from utilities.check import check_mail, check_places, check_name
from utilities.constants import MESSAGES_EMAIL, MESSAGES_PLACES, MESSAGES_COMPETITION, MESSAGES_CLUB
from utilities.load_db import loadClubs, loadCompetitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/showSummary', methods=['POST'])
def showSummary():
    ret, club = check_mail(request.form['email'], clubs)
    if ret == 0:
        return render_template('welcome.html', club=club, competitions=competitions)
    else:
        flash(MESSAGES_EMAIL[ret])
        return render_template('index.html')


@app.route('/book/<competition>/<club>')
def book(competition, club):
    retcl, foundClub = check_name(club, clubs)
    if retcl == 0:
        retcomp, foundCompetition = check_name(competition, competitions)
        if retcomp == 0:
            return render_template('booking.html', club=foundClub, competition=foundCompetition)
        else:
            flash(MESSAGES_COMPETITION[retcomp])
            return render_template('welcome.html', club=club, competitions=competitions)
    else:
        flash(MESSAGES_CLUB[retcl])
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces', methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    if request.form['submit_button'] == 'Cancel':
        return render_template('welcome.html', club=club, competitions=competitions)
    else:
        ret = check_places(request.form['places'], int(competition['numberOfPlaces']), int(club['points']))
        flash(MESSAGES_PLACES[ret])
        if ret == 0:
            placesRequired = int(request.form['places'])
            competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - placesRequired
            club['points'] = int(club['points']) - placesRequired
            return render_template('welcome.html', club=club, competitions=competitions)
        else:
            return render_template('booking.html', club=club, competition=competition)


@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html', clubs=clubs)


@app.route('/logout')
def logout():
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
