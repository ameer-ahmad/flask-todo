from flask import Blueprint, jsonify, render_template, request, flash
from flask_login import login_required, current_user
from .models import Todo
from . import db
import json

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

@views.route('/delete-todo', methods=['POST'])
def delete_todo():
    todo = json.loads(request.data)
    todoId = todo['todoId']
    todo = Todo.query.get(todoId)
    if todo:
        if todo.user_id == current_user.id:
            db.session.delete(todo)
            db.session.commit()
            
    return jsonify({})