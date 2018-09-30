"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, redirect, url_for
from StartSelect.database import *
from StartSelect.forms import *
from StartSelect.Breadcrumbs import *
from StartSelect import app
from flask_wtf import FlaskForm
from flask_breadcrumbs import Breadcrumbs, register_breadcrumb
from wtforms import StringField, TextAreaField, IntegerField, SelectField, PasswordField, BooleanField, DecimalField,validators
from passlib.hash import sha256_crypt

app.config['SECRET_KEY'] = 'SuperSecretKey'
Breadcrumbs(app=app)

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
    bInForm = addBeerForm()
    bInForm.breweryName.choices = [(brew[0],brew[1]) for brew in getBreweries()]
    bOutForm = removeBeerForm()
    bOutForm.beerName.choices = [(b[0],b[1]) for b in getRemoveBeers(1)]
    aInForm = addArcadeForm()
    aInForm.publisher.choices = [(pub[0],pub[1]) for pub in getPublishers()]
    aInForm.genre.choices = [(gen[0],gen[1]) for gen in getGenres()]
    aOutForm = removeArcadeForm()
    aOutForm.gameName.choices = [(game[0],game[1]) for game in getRemoveArcades(1)]
    sInForm = addSpecialForm()
    sInForm.day.choices = [('Mon','Mon'),('Tue','Tue'),('Wed','Wed'),('Thur','Thur'),('Fri','Fri'),('Sat','Sat'),('Sun','Sun')]
    sOutForm = removeSpecialForm()
    sOutForm.specialD.choices = [(spec[0],spec[1]) for spec in getRemoveSpecials(1)]
    """Renders the admin dashboard"""
    return render_template(
        'dashboard.html',
        title='Administer Dashboard',
        year=datetime.now().year,
        message='Add/Remove Panel',
        beerInForm = bInForm,
        beerOutForm = bOutForm,
        gameInForm = aInForm,
        gameOutForm = aOutForm,
        specialInForm = sInForm,
        specialOutForm = sOutForm
        )
@app.route('/newBeer', methods=['POST'])
def newBeer():
    form = addBeerForm()
    locIN = 1
    nameIN = form.beerName.data
    breweryIN = form.breweryName.data
    styleIN = form.style.data
    priceIN = form.price.data
    draftIN = form.draft.data
    abvIN = form.abv.data
    ibuIN = form.ibu.data
    featuredIN = form.featured.data
    addBeer(locIN,nameIN,breweryIN,styleIN,priceIN,draftIN,abvIN,ibuIN,featuredIN)
    return redirect(url_for('dashboard'))

@app.route('/removeBeer', methods=['POST'])
def subBeer():
    form = removeBeerForm()
    beerID = form.beerName.data
    removeBeer(1,beerID)
    return redirect(url_for('dashboard'))

@app.route('/newArcade', methods=['POST'])
def newArcade():
    form = addArcadeForm()
    locIN = 1
    arcadeIN = form.arcadeName.data
    publisherIN = form.publisher.data
    genreIN = form.genre.data
    yearIN = form.year.data
    playersIN = form.players.data
    featuredIN = form.featured.data
    addArcade(locIN,arcadeIN,publisherIN,genreIN,yearIN,playersIN,featuredIN)
    newArcade = [locIN,arcadeIN,publisherIN,genreIN,yearIN,playersIN,featuredIN]
    return redirect(url_for('dashboard'))
@app.route('/removeArcade', methods=['POST'])
def subArcade():
    form = removeArcadeForm()
    arcadeID = form.gameName.data
    oldArcade = arcade.query.filter(arcade.id == arcadeID).add_columns(arcade.name)
    oldArcade = oldArcade[0][1]
    removeArcade(1,arcadeID)
    return redirect(url_for('dashboard'))
@app.route('/newSpecial', methods=['POST'])
def newSpecial():
    form = addSpecialForm()
    dayIN = form.day.data
    descIN = form.desc.data
    addSpecial(1,dayIN,descIN)
    newSpecial = [dayIN,descIN]
    return redirect(url_for('dashboard'))

@app.route('/removeSpecial', methods=['POST'])
def subSpecial():
    form = removeSpecialForm()
    specialID = form.specialD.data
    removeSpecial(1,specialID)
    return redirect(url_for('dashboard'))


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