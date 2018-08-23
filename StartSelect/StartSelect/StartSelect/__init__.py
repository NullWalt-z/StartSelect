"""
The flask application package.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
app = Flask(__name__)

import StartSelect.views
import StartSelect.database

