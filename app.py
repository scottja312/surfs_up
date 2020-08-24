# Import Flask dependency.
from flask import Flask

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

# 2. Practice: create a function called hello_world().
@app.route('/')
def hello_world():
    return 'Hello World'

# 3. Run a Flask App (using terminal).

