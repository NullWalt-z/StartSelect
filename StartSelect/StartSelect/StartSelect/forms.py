from StartSelect.database import *
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,IntegerField,SelectField,PasswordField,BooleanField,DecimalField,SubmitField,validators
from passlib.hash import sha256_crypt

class loginForm(FlaskForm):
    True
class addBeerForm(FlaskForm):
    beerName = StringField('Beer Name', [validators.Length(min=1, max=50),validators.DataRequired()])
    breweryName = SelectField('Select a Brewery')
    breweryName.choices = [(brew[0],brew[1]) for brew in getBreweries()]
    style = StringField('Style', [validators.Length(min=1,max=50),validators.DataRequired()])
    price = DecimalField('Price', [validators.DataRequired()], places=2)
    draft = BooleanField('Draft')
    abv = DecimalField('ABV', [validators.DataRequired()], places=1)
    ibu = IntegerField('IBU')
    featured = BooleanField('Featured')
    submitAB = SubmitField('submit')
class removeBeerForm(FlaskForm):
    beerName = SelectField('Select Beer')
    submitRB = SubmitField('submit')
class addArcadeForm(FlaskForm):
    arcadeName = StringField('Arcade Name', [validators.Length(min=4,max=50), validators.DataRequired()])
    publisher = SelectField('Select a Publisher',[validators.DataRequired()])
    genre = SelectField('Select a Genre',[validators.DataRequired()])
    year = IntegerField('Year')
    players = IntegerField('# Players')
    featured = BooleanField('Featured')
class removeArcadeForm(FlaskForm):
    locID = 0
    gameName = SelectField('Select Arcade')
    submitRA = SubmitField('submit')
class addSpecialForm(FlaskForm):
    day = SelectField('Day',[validators.DataRequired()])
    desc = TextAreaField('Description')
    submitAS = SubmitField('submit')
class removeSpecialForm(FlaskForm):
    locID = 0
    specialD = SelectField('Special',[validators.DataRequired()])
    submitRS = SubmitField('submit')

