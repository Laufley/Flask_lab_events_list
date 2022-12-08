from flask import render_template, request, redirect
from app import app
from models.event_list import all_events
from models.event import Event

@app.route('/events')
def index():
    return render_template('index.html', title = "All events", events_html=all_events)

@app.route('/events', methods=['POST'])
def create():
        
    name = request.form['name']
    date = request.form['date']
    capacity = request.form['capacity']
    location = request.form['location']
    description = request.form['description']
    recurring = request.form['recurring']
    
    new_event = Event(date, name, capacity, location, description, recurring)
    all_events.append(new_event)
        
    return redirect('/events')

@app.route('/events/delete/<index>', methods=['POST'])
def eliminate():
    event_to_delete = request.form['delete']
    
    return redirect('/events')
