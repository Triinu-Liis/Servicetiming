from pkgutil import get_data
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Note
from .models import Screen
from . import db
import json
from datetime import datetime, timedelta

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def dashboard():
    if request.method == 'POST': 
        note = request.form.get('note')#Gets the note from the HTML 

        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note = Note(data=note, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_note) #adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("dashboard.html", user=current_user)

@views.route('/itinerary-settings',methods=['GET','POST'])
def itinerary():
    return render_template('itinerary.html', user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})

@views.route('/delete-screen', methods=['POST'])
def delete_screen():
    screen = json.loads(request.data)
    screenId = screen['screenId']
    screen = Screen.query.get(screenId)
    if screen:
        if screen.user_id == current_user.id:
            db.session.delete(screen)
            db.session.commit()
    return jsonify({})

@views.route('/time', methods=['GET', 'POST'])
def time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return render_template('time.html', user=current_user, datetime = current_time)

@views.route('/new-screen', methods=['GET','POST'])
def new_screen():
    if request.method == 'GET':
        return render_template('new-screen.html', user=current_user)
    if request.method == 'POST':
        driver = request.form.get('driver')
        co_driver = request.form.get('co_driver')
        service_in = request.form.get('service_in')
        service_in_ms = datetime.strptime(service_in,"%H:%M")
        service_out = request.form.get('service_out')
        service_out_ms = datetime.strptime(service_out,"%H:%M")
        service_time = request.form.get('service_time')
        margin_time = request.form.get('margin_time')
        out_in_sec = (service_out_ms-service_in_ms).total_seconds()
        service_time_sec = float(service_time)*60
        screen = Screen.query.filter_by(driver=driver).first()
        if screen:
            flash('Driver already logged!', category='error')
        elif len(driver) < 3:
            flash('Driver name too short!', category='error')
        elif len(co_driver) < 3:
            flash('Co-driver name too short!', category='error')
        elif service_out_ms < service_in_ms:
            flash('Service IN must be before Service OUT', category='error')
        elif out_in_sec != service_time_sec:
            flash('Service time does not match', category='error')
        else:
            new_screen = Screen(driver=driver,co_driver=co_driver,service_IN=service_in,
                                service_OUT=service_out,service_time=float(service_time),
                                margin_time=margin_time,user_id=current_user.id)
            db.session.add(new_screen)
            db.session.commit()
            flash('Screen added!', category='success')
            return render_template('itinerary.html',user=current_user)
    return render_template('new-screen.html',user=current_user)

@views.route('/service-time',methods=['GET','POST'])
def service_time():
    return render_template('/service_time.html',user=current_user,screens=current_user.screens)

@views.route('/screen_1',methods=['GET','POST'])
def screen_1():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return render_template('screen_1.html',user=current_user,time=current_time)

"""q
@views.route('/remember-id',methods=['GET','POST'])
def remember_id():
    screenId = 
    screen = Screen.query.get(screenId)
    print("screen")
    print(screen)
    print(screenId)
    if screen:
        print("screen")
        print(screen)
        print("screen")
        flash(screenId, category="success")
    return render_template('/service_time.html',user=current_user,
                               screenId=screenId)
"""