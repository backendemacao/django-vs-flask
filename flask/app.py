from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    done = db.Column(db.Boolean, default=False)


@app.get('/')
def index():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)


@app.post('/')
def create_todo():
    title = request.form['title']
    db.session.add(Todo(title=title))
    db.session.commit()

    return redirect(url_for('index'))


@app.post('/complete/<int:todo_id>')
def complete_todo(todo_id):
    todo = db.session.query(Todo).filter_by(id=todo_id).one()
    todo.done = True
    db.session.commit()

    return redirect(url_for('index'))


@app.post('/delete/<int:todo_id>')
def delete_todo(todo_id):
    todo = db.session.query(Todo).filter_by(id=todo_id).one()
    db.session.delete(todo)
    db.session.commit()

    return redirect(url_for('index'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)
