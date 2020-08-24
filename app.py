################################
# Set Up the Flask Weather App
###############################
# Import dependencies.
import datetime as dt
import numpy as np
import pandas as pd

# Import dependencies for SQLAlchemy.
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

######################
# Set Up the Database
######################
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect exisiting database into a new model
Base = automap_base()

# Reflect the tables
Base.prepare(engine, reflect=True)

# Setup the classes of keys (measurement, station)
Base.classes.keys()

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create session from python to the DB
session = Session(engine)

###############
# Set Up Flask
###############
# Create a New Flask App Instance.
app = Flask(__name__)
# Note: the "name" variable inside of the flask() function denotes
# the name of the current function; this variable can determine
# if your code is being run from the command line or if it has
# been imported into another piece of code.
# Variables with ___ underscores before and after them are called
# "magic methods" in Python.

# Create Flask Routes.
# 1. Define the starting point, known as the "root".
@app.route('/')
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:<br/>
    /api/v1.0/precipitation<br/>
    /api/v1.0/stations<br/>
    /api/v1.0/tobs<br/>
    /api/v1.0/temp/start/end<br/>
    ''')

# 2. Define precipitation route.
# Note: return the precipitation data for the last year.
@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

if __name__ == '__main__':
    app.run()