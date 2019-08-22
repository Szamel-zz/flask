import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


basedir = os.path.abspath(os.path.dirname(__file__))
# __file__ --> C:\Courses\Udemy\python_and_flask_bootcamp\flask\flask_examples


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MOFICATIONS'] = False


db = SQLAlchemy(app)


# Create a model
class Puppy(db.Model):

    # Manual table name choice
    __tablename__ = 'puppies'

    # columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return 'Puppy {} is {} years old'.format(self.name, self.age)



