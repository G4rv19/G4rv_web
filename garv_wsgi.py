import sys

# Use forward slashes and escape the backslash
path = '/home/My\\website'

# Append the path to sys.path
if path not in sys.path:
    sys.path.append(path)

# Import the Flask app object from main.py
from main import app as application
t