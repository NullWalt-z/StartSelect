import flask
from flask_sqlalchemy import SQLAlchemy
from StartSelect import app

#######################
### DATABASE MODELS ###
#######################

class location(db.Model):
    __tablename__ = 'location'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    city = db.Column(db.String(80))
    address = db.Column(db.Integer)
    #relationships
    db.relationship('beer',backref='location')
    db.relationship('arcade',backref='location')
    db.relationship('special',backref='location')
    #function definitions
    def __repr__(self):
        return '<location %r>' % self.name
    def __init__(self,city, address):
        self.city = city
        self.address = address

class beer(db.Model):
    __tablename__ = 'beer'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    locationid = db.Column(db.Integer,db.ForeignKey('location.id'),nullable=False)
    name = db.Column(db.String(80))
    breweryid = db.Column(db.Integer,db.ForeignKey('brewery.id'),nullable=False)
    style = db.Column(db.String(80))
    price = db.Column(db.Numeric(2,2))
    draft = db.Column(db.Boolean)
    #relationships
    """none"""
    #function definitions
    def __repr__(self):
        return '<beer %r>' % self.name
    def __init__(self,name,breweryid, style, price):
        self.name = name
        self.breweryid = breweryid
        self.style = style
        self.price = price

class brewery(db.Model):
    __tablename__ = 'brewery'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(80))
    state = db.Column(db.String(80))
    #relationships
    db.relationship('beer',backref='brewery')
    #function definitions
    def __repr__(self):
        return '<brewery %r>' %self.name
    def __init__(self,name,state):
        self.name = name
        self.state = state

class arcade(db.Model):
    __tablename__ = 'arcade'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    locationid = db.Column(db.Integer,db.ForeignKey('location.id'),nullable=False)
    name = db.Column(db.String(80))
    publisherid = db.Column(db.Integer,db.ForeignKey('publisher.id'),nullable = False)
    genreid = db.Column(db.Integer,db.ForeignKey('genre.id'),nullable = False)
    year = db.Column(db.Integer)
    playercount = db.Column(db.Integer)
    #relationships
    ##NEEED TO DO THIS SECTION!!!!
    #function definitions
    def __repr__(self):
        return '<arcade %r>' % self.name
    def __init__(self,name,publisherid,genreid,year,playercount):
        self.name = name
        self.publisherid = publisherid
        self.genreid = genreid
        self.year = year
        self.playercount = playercount

class publisher(db.Model):
    __tablename__ = 'publisher'
    id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    name = db.Column(db.String(80))
    #relationships
    db.relationship('arcade',backref='arcade')
    #function definitions
    def __repr__(self):
        return '<publisher %r>' % self.name
    def __init__(self,name):
        self.name = name

class genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(80))
    #relationships
    db.relationship('arcade',backref='genre')
    #function definitions
    def __repr__(self):
        return '<genre % r>' % self.title
    def __init__(self,title):
        self.title = title

class special(db.Model):
    __tablename__ = 'special'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    locationid = db.Column(db.Integer, db.ForeignKey('location.id'),nullable=False)
    day = db.Column(db.String(7))
    desc = db.Column(db.String(250))
    #function definitions
    def __repr__(self):
        return'<special % r>' %self.desc
    def __init__(self,day,desc):
        self.day = day
        self.desc = desc

###################
### VIEW MODELS ###
###################

class locBeer:
    def __init__(self, name, brewery, style, price, draft):
        self.Name = name
        self.Brewery = brewery
        self.Style = style
        self.Price = price
        self.Draft = draft
    def __eq__(self, other):
        if((self.Brewery == other.Brewery) and (self.Name == other.Name) and (self.Draft == other.Draft)):
            return True
        else:
            return False
    def __ne__(self, other):
        if (self == other):
            return False
        else:
            return True
    def __gt__(self, other):
        if (self.Brewery > other.Brewery):
            return True
        elif (self.Brewery == other.Brewery):
            if (self.Name > other.Name):
                return True
            else:
                return False
        else:
            return False
    def __lt__(self, other):
        if ((self > other) or (self == other)):
            return False
        else:
            return True
            
class locArcade:
    def __init__(self, name, publisher, genre, year, plyrcnt):
        self.Name = name
        self.Publisher = publisher
        self.Genre = genre
        self.Year = year
        self.Plyrcnt = plyrcnt

class locSpecials:
    def __init__(self, day, desc):
        self.Day = day
        self.Desc = desc
    def __eq__(self, other):
        #NEED TO REWORK FOR NOT SAME DESCRIPTION
        if (self.day == other.day):
            return True
        else:
            return False
    def __ne__(self, other):
        if (self == other):
            return False
        else:
            return True
    def __gt__(self, other):
        if(self.day == 'Mon'):   
            if ((other.day =='Tue') or (other.day == 'Wed') or (other.day == 'Thu') or (other.day == 'Fri') or (other.day == 'Sat') or (other.day == 'Sun')):
                return True
            else:
                return False
        elif(self.day == 'Tue'):
            if ((other.day == 'Wed') or (other.day == 'Thu') or (other.day == 'Fri') or (other.day == 'Sat') or (other.day == 'Sun')):
                return True
            else:
                return False
        elif(self.day == 'Wed'):
            if ((other.day == 'Thu') or (other.day == 'Fri') or (other.day == 'Sat') or (other.day == 'Sun')):
                return True
            else:
                return False
        elif(self.day == 'Thu'):
            if((other.day == 'Fri') or (other.day == 'Sat') or (other.day == 'Sun')):
                return True
            else:
                return False
        elif(self.day == 'Fri'):
            if((other.day == 'Sat') or (other.day == 'Sun')):
                return True
            else:
                return False
        elif(self.Day== 'Sat'):
            if(other.day == 'Sun'):
                return True
            else:
                return False
        else:
            return False
