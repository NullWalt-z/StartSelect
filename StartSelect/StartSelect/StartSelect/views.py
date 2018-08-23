"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from StartSelect.database import *
from StartSelect import app

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

@app.route('/admin', methods=['GET','POST'])
def admin():
    #breweries = getBreweriesByLocation(1)
    beers = getRemoveBeers(1)
    arcades = getRemoveArcades(1)
    publishers = getPublishers()
    breweries = getBreweries()
    genres = getGenres()
    
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
        allGenres = genres
        )

@app.route('/addBeer', methods=['POST'])
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



########################
### HELPER FUNCTIONS ###
########################

def convertWeek(numIN):
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

