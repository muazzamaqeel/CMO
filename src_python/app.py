from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///calendar.db'
db = SQLAlchemy(app)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200))
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"<Event {self.title}>"

@app.route('/')
def home():
    return "Welcome to the Calendar App!"

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
