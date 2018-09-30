import flask
from flask_sqlalchemy import SQLAlchemy
from StartSelect import app

###################
### VIEW MODELS ###
###################

class locationObj():
    def __init__(self,sqlQuery):
        self.id = sqlQuery[1]
        self.city = sqlQuery[2]
        self.city = sqlQuery[3]
    def __init__(self, id, city, address):
        self.id = id
        self.city = city
        self.address = address

class beerObj():
    def __init__(self,sqlQuery):
        self.id = sqlQuery[1]
        self.name = sqlQuery[2]
        self.breweryObj = True
        self.style = sqlQuery[4]
        self.price = sqlQuery[5]

    def __init__(self,id,name,breweryObj, style, price):
        self.id = id
        self.name = name
        self.breweryObj = breweryObj
        self.style = style
        self.price = price

class breweryObj():
    def __init__(self,id,name,state):
        self.id = id
        self.name = name
        self.state = state

class arcadeObj():
    def __init__(self,id,name,publisherObj,genreObj,year,playercount):
        self.id = id
        self.name = name
        self.publisherObj = publisherObj
        self.genreObj = genreObj
        self.year = year
        self.playercount = playercount

class publisherObj():
    def __init__(self,id,name):
        self.id = id
        self.name = name

class genreObj():
    def __init__(self,id,title):
        self.id = id
        self.title = title

class specialObj():
    def __init__(self,id,day,desc):
        self.id = id
        self.day = day
        self.desc = desc