"""
This script runs the StartSelect application using a development server.
"""

from os import environ
from StartSelect import app
from StartSelect import database
from StartSelect import views

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 25000
    app.run(HOST, PORT)
