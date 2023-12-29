from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from datetime import datetime
from .models import Workout
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        workout = request.form.get('workout')
        sets = int(request.form.get('sets'))
        reps = int(request.form.get('reps'))
        weight = int(request.form.get('weight'))
        date_str = request.form.get('date')

        # Convert the date string to a datetime object
        date = datetime.strptime(date_str, '%Y-%m-%d')

        if len(workout) < 1:
            flash('Exercise is too short!', category='error')
        else:
            new_workout = Workout(
                exercise=workout,
                sets=sets,
                reps=reps,
                weight=weight,
                date=date,  
                user_id=current_user.id
            )
            db.session.add(new_workout)
            db.session.commit()
            flash('Workout added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-workout', methods=['POST'])
def delete_workout(): 
    workout = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    workoutId = workout['workoutId']
    workout = Workout.query.get(workoutId)
    
    if workout:
        if workout.user_id == current_user.id:
            db.session.delete(workout)
            db.session.commit()

    return jsonify({})