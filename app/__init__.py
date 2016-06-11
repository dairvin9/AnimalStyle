from flask import Flask
from flask_sqlalchemy import SQLAlchemy as sqlalchemy

app = Flask(__name__)
app.config.from_object('config')
db = sqlalchemy(app)

from app import views, models