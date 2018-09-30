from datetime import datetime
from flask import render_template, redirect, url_for
from StartSelect.database import *
from flask_breadcrumbs import Breadcrumbs, register_breadcrumb

def uriToName(locURI):
    locName = processQuery(location.query.filter_by(uri = locURI).add_columns(location.city))
    return locName