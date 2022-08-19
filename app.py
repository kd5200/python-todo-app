from distutils.log import debug
from email.policy import default
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.string(200), nullable=False)
    date_create = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %>' % self.id


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug =True) 