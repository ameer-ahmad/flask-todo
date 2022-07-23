from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Todo
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    
    if request.method == 'POST':
        todo = request.form.get('todo')
        print(todo)
        
        if len(todo) < 1:
            flash('Todo is too short!', category='error')
        else:
            new_todo = Todo(data=todo, user_id=current_user.id)
            db.session.add(new_todo)
            db.session.commit()
            flash('Todo added!', category='success')
    
    return render_template("home.html", user=current_user)