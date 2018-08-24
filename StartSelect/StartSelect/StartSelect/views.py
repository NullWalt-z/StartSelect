"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from StartSelect.database import *
from StartSelect import app
from wtforms import Form, StringField, TextAreaField, IntegerField, SelectField, PasswordField, BooleanField, DecimalField,validators
from passlib.hash import sha256_crypt

@app.route('/')
@app.route('/home', methods=['GET'])
def home():
    """Renders the home page."""
    locationList = location.query.all()
    return render_template(
        'index.html',
        title='Start Select',
        locs = locationList,
        year=datetime.now().year
    )

@app.route('/<locURI>/', methods=['GET'])
def localhome(locURI):
    """Renders the localized home page"""
    locID = getIDFromURI(locURI)
    draftBeerList = getDraftBeers(locID)
    canBeerList = getCanBeers(locID)
    arcadeList = getArcades(locID)
    specialList = getSpecials(locID)
    locationInfo = getLocInfo(locID)

    return render_template(
        'localindex.html',
        title="Start Select " + locationInfo[0], #change to locName later
        year=datetime.now().year,
        locInfo = locationInfo,
        draftBeers = draftBeerList,
        canBeers = canBeerList,
        arcades = arcadeList,
        specials = specialList
        )

@app.route('/<locURI>/beer')
def localbeer(locURI):
    """Renders the locations beer page"""
    locID = getIDFromURI(locURI)
    locationInfo = getLocInfo(locID)
    draftBeerList = getDraftBeers(locID)
    canBeerList = getCanBeers(locID)
    return render_template(
        'localbeer.html',
        title = locationInfo[0] + ' - Beers',
        year=datetime.now().year,
        locInfo = locationInfo,
        draftBeers = draftBeerList,
        canBeers = canBeerList
        )

@app.route('/<locURI>/games')
def localArcades(locURI):
    """Renders the locations beer page"""
    locID = getIDFromURI(locURI)
    locGames = getArcades(locID)
    locationInfo = getLocInfo(locID)
    return render_template(
        'localarcade.html',
        title = locationInfo[0] + ' - Games',
        year=datetime.now().year,
        locInfo = locationInfo,
        arcades = locGames
        )

@app.route('/<locName>/specials')
def localSpecials(locName):
    """Renders the locations specials page"""
    locSpecials = getSpecials

@app.route('/<locName>/location')
def localnavigation(locName):
    ##LOOK UP GOOGLE MAPS API
    return render_template(
        'localnavigation.html',
        title='Start Select ' + locName + '-Navigation',
        year=datetime.now().year,
        )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/location')
def locations():
    """Renders the location page"""
    return render_template(
        'location.html',
        title='Location',
        year=datetime.now().year,
        message='Choose your location.'
        )

### ADMIN BLOCK ###


@app.route('/admin', methods=['GET','POST'])
def admin():
    #breweries = getBreweriesByLocation(1)
    beers = getRemoveBeers(1)
    arcades = getRemoveArcades(1)
    publishers = getPublishers()
    breweries = getBreweries()
    genres = getGenres()
    days = ['Mon','Tue','Wed','Thur','Fri','Sat','Sun']
    specials = getRemoveSpecials(1)
    
    """Renders the location page"""
    return render_template(
        'admin.html',
        title='Admin - Login',
        year=datetime.now().year,
        message='Admin Login',
        locBeers = beers,
        locArcades = arcades,
        allPublishers = publishers,
        allBreweries = breweries,
        allGenres = genres,
        week = days,
        locSpecials = specials
        )
@app.route('/dashboard', methods=['POST','GET'])
def  dashboard():
    return render_template(
        'dashboard.html',
        title='Administer Dashboard',
        year=datetime.now().year,
        message='Add/Remove Panel',
        newBeerForm = addBeerForm(),
        beerOutForm = removeBeerForm(),
        arcadeInForm = addArcadeForm(),
        arcadeOutForm = removeArcadeForm(),
        specialInForm = addSpecialForm(),
        specialOutForm = removeSpecialForm()
        )

@app.route('/newBeer', methods=['POST'])
def newBeer():
    locIN = request.form['locationIn']
    nameIN = request.form['beerNameIn']
    breweryIN = request.form['addBeerBrewSelect']
    styleIN = request.form['styleIn']
    priceIN = request.form['priceIn']
    draftIN = request.form.get('draftIn', False)
    abvIN = request.form['abvIn']
    ibuIN = request.form['ibuIn']
    featuredIN = request.form.get('featuredIn', False)
    addBeer(locIN,nameIN,breweryIN,styleIN,priceIN,draftIN,abvIN,ibuIN,featuredIN)
    """adds beer to DB then returns to admin page"""
    return render_template(
        'newBeer.html',
        title='Confirm New Beer',
        year=datetime.now().year,
        message='Confirm New Beer',
        thisBeer = [locIN,nameIN,breweryIN,styleIN,priceIN,draftIN,abvIN,ibuIN,featuredIN]
        )
@app.route('/removeBeer', methods=['POST'])
def subBeer():
    beerID = request.form['removeBeerSelect']
    oldBeer = beer.query.filter(beer.id == beerID).add_column(beer.name)
    oldBeer = oldBeer[0][1]##MAYBE!?!?!?!?!
    removeBeer(1,beerID)
    return render_template(
        'removeBeer.html',
        title='Admin - Login',
        year=datetime.now().year,
        message='Admin Login',
        thisBeer = oldBeer
        )

@app.route('/newArcade', methods=['POST'])
def newArcade():
    locIN = request.form['locationIn']
    arcadeIN = request.form['arcadeNameIn']
    publisherIN = request.form['addArcadePubSelect']
    genreIN = request.form['addArcadeGenreSelect']
    yearIN = request.form['yearIn']
    playersIN = request.form['playersIn']
    featuredIN = request.form.get('featuredIn')
    addArcade(locIN,arcadeIN,publisherIN,genreIN,yearIN,playersIN,featuredIN)
    newArcade = [locIN,arcadeIN,publisherIN,genreIN,yearIN,playersIN,featuredIN]
    return render_template(
        'newArcade.html',
        title = 'Confirm New Arcade',
        year=datetime.now().year,
        message='Confirm New Arcade',
        thisArcade = newArcade
        )

@app.route('/removeArcade', methods=['POST'])
def subArcade():
    arcadeID = request.form['removeArcadeSelect']
    oldArcade = arcade.query.filter(arcade.id == arcadeID).add_columns(arcade.name)
    oldArcade = oldArcade[0][1]
    removeArcade(1,arcadeID)
    return render_template(
        'removeArcade.html',
        title = 'Confirm Game Removal',
        year=datetime.now().year,
        thisArcade = oldArcade
        )
@app.route('/newSpecial', methods=['POST'])
def newSpecial():
    locIN = request.form['locationIn']
    dayIN = request.form['addSpecialDaySelect']
    descIN = request.form['descIn']
    addSpecial(locIN,dayIN,descIN)
    newSpecial = [dayIN,descIN]
    return render_template(
        'newSpecial.html',
        title = 'Confirm New Special',
        year=datetime.now().year,
        thisSpecial = newSpecial
        )

@app.route('/removeSpecial', methods=['POST'])
def subSpecial():
    specialID = request.form['removeSpecialSelect']
    oldSpecial = special.query.filter(special.id == specialID).add_columns(special.day,special.dayNum).order_by(special.dayNum)
    oldSpecial = oldSpecial[0][1]
    removeSpecial(1,specialID)
    return render_template(
        'removeSpecial.html',
        title = 'Confirm Special Removal',
        year = datetime.now().year,
        thisSpecial = oldSpecial
        )


########################
### HELPER FUNCTIONS ###
########################
def numToDay(numIN):
    if(numIN == 1):
        return 'Mon'
    elif(numIN == 2):
        return 'Tue'
    elif(numIN == 3):
        return 'Wed'
    elif(numIN == 4):
        return 'Thur'
    elif(numIN == 5):
        return 'Fri'
    elif(numIN == 6):
        return 'Sat'
    elif(numIN == 7):
        return 'Sun'
    else:
        return 'Everyday'

####################
### FORM CLASSES ###
####################
class loginForm(Form):
    True
class addBeerForm(Form):
    breweryChoices = getBreweries()
    beerName = StringField('Beer Name', [validators.Length(min=1, max=50),validators.DataRequired()])
    breweryName = SelectField('Select a Brewery', [validators.DataRequired()])
    breweryName.choices = [(brew[0],brew[1]) for brew in breweryChoices]
    style = StringField('Style', [validators.Length(min=1,max=50),validators.DataRequired()])
    price = DecimalField('Price', [validators.DataRequired()], places=2)
    draft = BooleanField('Draft')
    abv = DecimalField('ABV', [validators.DataRequired()], places=1)
    ibu = IntegerField('IBU')
    featured = BooleanField('Featured')
class removeBeerForm(Form):
    locID = 0
    beers = getRemoveBeers(locID)
    beerName = SelectField('Select Beer',[validators.DataRequired()])
    beerName.choices = [(b[0],b[1]) for b in beers]
class addArcadeForm(Form):
    arcadeName = StringField('Arcade Name', [validators.Length(min=4,max=50), validators.DataRequired()])
    publisher = SelectField('Select a Publisher',[validators.DataRequired()])
    igenre = SelectField('Select a Genre',[validators.DataRequired()])
    year = IntegerField('Year')
    players = IntegerField('Players')
    featured = BooleanField('Featured')
class removeArcadeForm(Form):
    locID = 0
    arcades = getRemoveArcades(locID)
    gameName = SelectField('Select Arcade',[validators.DataRequired()])
    gameName.choices = [(game[0],game[1]) for game in arcades]
class addSpecialForm(Form):
    day = SelectField('Day',[validators.DataRequired()], choices=[
        ('Mon',1),('Tue',2),('Wed',3),('Thur',4),('Fri',5),('Sat',6),('Sun',7)
        ])
    desc = TextAreaField('Description')
class removeSpecialForm(Form):
    True