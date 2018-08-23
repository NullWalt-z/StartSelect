from flask import Flask
from flask_sqlalchemy import *
from flask_sqlalchemy import SQLAlchemy
from StartSelect import app
#initializes the database and allows for the creation of tables within mysql

#Make sure you change the username(admin) and password(Group2017) before you run db.createall() as this will not connect to your database
#When running in python interactive make sure you do from StartSelect.database import db before you run db.create_all() or it will not know whats going on
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:0000@localhost/LeftRight'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

############################################
### Database LeftRight Table Definitions ###
############################################
class location(db.Model):
    __tablename__ = 'location'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    city = db.Column(db.String(80))
    address = db.Column(db.String(250))
    uri = db.Column(db.String(80))
    #relationships
    db.relationship('beer',backref='location')
    db.relationship('arcade',backref='location')
    db.relationship('special',backref='location')
    #function definitions
    def __repr__(self):
        return "[%r,%r]" %(self.city, self.address)
    def __init__(self,city, address, url):
        self.city = city
        self.address = address
        self.url = url

class beer(db.Model):
    __tablename__ = 'beer'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    locationid = db.Column(db.Integer,db.ForeignKey('location.id'),nullable=False)
    name = db.Column(db.String(80))
    breweryid = db.Column(db.Integer,db.ForeignKey('brewery.id'),nullable=False)
    style = db.Column(db.String(80))
    price = db.Column(db.Integer)
    draft = db.Column(db.Boolean)
    abv = db.Column(db.Numeric)
    ibu = db.Column(db.Integer)
    featured = db.Column(db.Boolean)
    #relationships
    """none"""
    #function definitions
    def __repr__(self):
        return "<beer(name= '%r'>" % self.name
    def __init__(self,locationid,name,breweryid,style,price,draft,abv,ibu,featured):
        self.locationid = locationid
        self.name = name
        self.breweryid = breweryid
        self.style = style
        self.price = price
        self.draft = draft
        self.abv = abv
        self.ibu = ibu
        self.featured = featured

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
    featured = db.Column(db.Boolean)
    #relationships
    ##NEEED TO DO THIS SECTION!!!!
    #function definitions
    def __repr__(self):
        return '<arcade %r>' % self.name
    def __init__(self,locationid,name,publisherid,genreid,year,playercount,featured):
        self.locationid = locationid
        self.name = name
        self.publisherid = publisherid
        self.genreid = genreid
        self.year = year
        self.playercount = playercount
        self.featured = featured

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
    day = db.Column(db.String(10))
    dayNum = db.Column(db.Integer)
    desc = db.Column(db.String(250))

    def dayNummer(dayIN):
        if(dayIN=='Mon'):
            return 1
        elif(dayIN=='Tue'):
            return 2
        elif(dayIN=='Wed'):
            return 3
        elif(dayIN=='Thur'):
            return 4
        elif(dayIN=='Fri'):
            return 5
        elif(dayIN=='Sat'):
            return 6
        elif(dayIN=='Sun'):
            return 7
        else:
            return 10

    #function definitions
    def __repr__(self):
        return'<special % r>' %self.desc
    def __init__(self,locationid,day,desc):
        self.locationid = locationid
        self.day = day
        self.dayNum = dayNummer(day)
        self.desc = desc

########################
### Database Queries ###
########################

def getIDFromURI(URIN):
    #takes URI-IN (get it...URIN) and return location ID for further querying
    locID = location.query.filter_by(uri = URIN).add_columns(location.id)
    locID = (locID[0][1])
    return locID
def getLocInfo(locID):
    #takes a locID and returns location name, address, etc
    locationInfo = location.query.filter(location.id == locID).add_columns(location.city, location.address, location.uri)
    locInfo = [locationInfo[0][1],locationInfo[0][2],locationInfo[0][3]]
    return locInfo
def getDraftBeers(locID):
#takes a locationID and returns an array of models.beer objects that are drafts
#need to add ibu and abv
    draftBeers = []
    locBeerDraft = beer.query.filter(beer.locationid == locID, beer.draft == True).join(brewery).add_columns(
        beer.name, brewery.name, beer.style, beer.price).order_by(brewery.name)  
    for beers in locBeerDraft:
        newBeer = []
        newBeer.append(beers[1])
        newBeer.append(beers[2])
        newBeer.append(beers[3])
        newBeer.append(beers[4])
        draftBeers.append(newBeer)
    #print(draftBeers)
    return draftBeers

def getCanBeers(locID):
#takes a locationID and returns an array of models.beer objects that are cans or bottles
    locCanDraft = beer.query.filter(beer.locationid == locID, beer.draft == False).join(brewery).add_columns(
        beer.name, brewery.name, beer.style, beer.price, beer.draft).order_by(brewery.name)
    canBeers = []
    for beers in locCanDraft:
        newBeer = []
        newBeer.append(beers[1])
        newBeer.append(beers[2])
        newBeer.append(beers[3])
        newBeer.append(beers[4])
        canBeers.append(newBeer)
    return canBeers

def getRemoveBeers(locID):
#Gets necessary data to populate remove beers list
    locCanDraft = beer.query.filter(beer.locationid == locID).join(brewery).add_columns(
        beer.id,beer.name, brewery.name,beer.draft).order_by(brewery.name)
    allBeers = []
    for beers in locCanDraft:
        newBeer = []
        newBeer.append(beers[1])
        newBeer.append(beers[2])
        newBeer.append(beers[3])
        if(beers[4] == True):
            newBeer.append('Draft')
        else:
            newBeer.append('Can/Bottle')
        allBeers.append(newBeer)
    return allBeers

def getArcades(locID):
    cabinets = []
    locArcades = arcade.query.filter(arcade.locationid == locID).join(publisher).join(genre).add_columns(
        arcade.name, publisher.name, genre.title, arcade.year, arcade.playercount).order_by(genre.title)
    for arcades in locArcades:
        newArcade = []
        newArcade.append(arcades[1])
        newArcade.append(arcades[2])
        newArcade.append(arcades[3])
        newArcade.append(arcades[4])
        newArcade.append(arcades[5])
        cabinets.append(newArcade)
    return cabinets

def getBreweriesByLocation(locID):
    locBreweries = beer.query.filter(beer.locationid==locID).add_column(beer.breweryid)
    breweries = []
    for brew in locBreweries:
        brew = brew[1]
        if brew not in breweries:
            breweries.append(brew)
    locBreweries = brewery.query.filter(brewery.id.in_(breweries)).add_columns(brewery.id,brewery.name)
    breweries = []
    for brew in locBreweries:
        brew = brew[1:]
        breweries.append(brew)
    return breweries


def getSpecials(locID):
    locSpecials = special.query.filter(special.locationid == locID).add_columns(special.day, special.desc).order_by(special.dayNum)
    #Need to write sort function (comparison and equality have been overridden already)
    dailySpecial = []
    for specials in locSpecials:
        newSpecial = []
        newSpecial.append(specials[1])
        newSpecial.append(specials[2])
        dailySpecial.append(newSpecial)
    #FIGURE OUT HOW TO SORT!!!!!!!!!!!!!
    return dailySpecial

    return specials

def searchBeers(searchString):
    #return a list of beers meeting query
    return null

def searchArcades(searchString):
    #return a list of arcades meeting query
    return null



#################################
### Insert / Remove Functions ###
#################################

def addBeer(locID,beerName,breweryName,beerType,beerPrice,isDraft,beerABV,beerIBU,isFeatured):
    print('LOCID = ' + locID)
    newID = brewery.query.filter(brewery.name == breweryName).add_column(brewery.id)
    newID=newID[0][1]
    if not(newID):
        print('Error - Please Add Brewery')
        return False
    newBeer = beer(locID,beerName,newID,beerType,beerPrice,isDraft,beerABV,beerIBU,isFeatured)
    db.session.add(newBeer)
    db.session.commit()
    return True

def removeBeer(locID,beerID):
    db.session.query(beer).filter(beer.id == beerID, beer.locationid == locID).delete()
    db.session.commit()
    return True

def addBrewery(breweryName, state):
    newBrewery = brewery(breweryName, state)
    db.session.add(newBrewery)
    db.session.commit()
    return True

def removeBrewery(breweryName):
    db.session.query(brewery).filter(brewery.name == breweryName).delete()
    db.session.commit()
    return True

def addArcade(locID,gameName,gamePublisher,gameGenre,gameYear,numPlayers,featured):
    newPubID = publisher.query.filter(publisher.name == gamePublisher).add_column(publisher.id)
    if not (newPubID):
        print('Error - Please Add Publisher')
        return False
    newArcade = arcade(locID,gameName,gamePublisher,gameGenre,gameYear,numPlayers,featured)
    db.session.add(newArcade)
    db.session.commit()
    return True

def removeArcade(locID,gameName):
    db.session.query(arcade).filter(arcade.locationid == locID,arcade.name==gameName)
    db.session.commit()
    return True

def addPublisher(publisherName):
    newPublisher = publisher(publisherName)
    db.session.add(newPublisher)
    db.session.commit()
    return True

def removePublisher(publisherName):
    db.session.query(publisher).filter(publisher.name == publisherName).delete()
    db.session.commit()
    return True

def addGenre(genreName):
    newGenre = genre(genreName)
    db.session.add(newGenre)
    db.session.commit()
    return True

def removeGenre(genreName):
    db.session.query(genre).filter(genre.title == genreName).delete()
    db.session.commit()
    return True

def addSpecial(locID,specialDay,specialDesc):
    newSpecial = special(locID,specialDay,specialDesc)
    db.session.add(newSpecial)
    db.session.commit()
    return True

def removeSpecial(locID,specialID):
    db.session.query(special).filter(special.locationid == locID, special.id == specialID).delete()
    db.session.commit()
    return True
    
#################
### Test Data ###
#################

locations = [
    #[city,address]
    ['Kansas City','101 SW Boulevard, Kansas City, MO 64068', 'Kansas-City/'],
    ['Des Moines','500 E Locust St, Des Moines, IA 50309', 'Des-Moines/'],
    ['Minneapolis','3012 Lyndale Ave S, Minneapolis, MN 55408', 'Minneapolis/']
    ]
breweries = [
    #[name,state]
    ['Boulevard','MO'],
    ['Emperial','MO'],
    ['Cinder Block','MO'],
    ['Exile','IA'],
    ['Fox','IA'],
    ['Firetrucker','IA'],
    ['Pryes','MN'],
    ['Surly','MN'],
    ['Modist','MN']
    ]
beers = [
    #[locID,name,brewerID,style,price,draft]
    #NEED TO GET IBU AND ABV DATA
    [1,'Pale Ale',1,'Pale Ale',5.50,True],
    [1,'Biscuit',2,'English Brown Ale',5.50,True],
    [1,'Block IPA',3,'IPA',6.50,False],
    [2,'Beatnik Sour',4,'Berliner Weisse',7.50,True],
    [2,'Fox Tail',5,'English Red',4.50,True],
    [2,'Pumper Truck',6,'Porter',5.50,False],
    [3,'Miraculum',7,'IPA',5.50,True],
    [3,'First Avenue',8,'Golden Ale',5.50,False],
    [3,'Supra',9,'Lager',4.50,True]
    ]

publishers = ['Capcom','Midway','Atari','Williams','Sega']
genres = ['Shooter', 'Fighter', 'Pinball']

arcades = [
    #[locID,Name,publisher,genre,year,players]
    [1,'Mortal Kombat II',2,2,1993,2],
    [1,'Maximum Force/Area 51',3,1,1997,2],
    [1,'Medieval Madness',4,3,1997,4],
    [2,'Marvel vs Capcom',1,2,1998,2],
    [2,'House of the Dead',5,1,1997,2],
    [2,'Game of Thrones',4,3,2015,4],
    [3,'Virtua Fighter',5,2,1993,1],
    [3,'Terminator 2: Judgement Day',2,1,1991,2],
    [3,'Addams Family',4,3,1992,4]
    ]

specials = [
    #[locID,day,desc]
    [1,'Tue',2,'Dollar off all local (MO or KS) beers'],
    [1,'Fri',5,'BOGO tokens'],
    [2,'Mon',1,'3 dollar domestic tallboys'],
    [2,'Thu',4,'Industry Night - 5 dollar PBJs, 6 dollar premium tequila shots'],
    [3,'Sun',7,'25 Dollar 6 pack and a pound'],
    [3,'Wed',3,'4 dollar well cocktails']
    ]

def insertTestData(newLocs,newBreweries,newBeers,newPubs,newGenres,newArcades,newSpecs):
    try:
        for i in newLocs:
            db.session.add(i)
            db.session.commit()
    except:
        print('Error in locations')
        return False
    try:
        for i in newBreweries:
            db.session.add(i)
            db.session.commit()
    except:
        print('Error in breweries')
        return False
    try:
        for i in newBeers:
            db.session.add(i)
            db.session.commit()
    except:
        print('Error in Beers')
        return False
    try:
        for i in newPubs:
            db.session.add(i)
            db.session.commit()
    except:
        print('Error in Publishers')
        return False
    try:
        for i in newGenres:
            db.session.add(i)
            db.session.commit()
    except:
        print('Error in genres')
        return False
    try:
        for i in newArcades:
            db.session.add(i)
            db.session.commit()
    except:
        print('Error in arcades')
        return False
    try:
        for i in newSpecs:
            db.session.add(i)
            db.session.commit()
        return True
    except:
        print('Error in specials')
        return False