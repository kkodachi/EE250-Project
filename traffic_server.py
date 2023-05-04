from typing import Dict, List, Optional
from flask import Flask, request, jsonify
import pathlib
import uuid
import json

app = Flask(__name__)
# path to directory of this file
thisdir = pathlib.Path(__file__).parent.absolute() 

# TODO: get all 24 jsons & store in a list

# TODO: parse each json for the "duration" element in JSON
# convert from seconds to minutes

# TODO: plot element of each hour in a bar graph with plotly
# x-axis will be the time (0, 1, 2, ..., 24), y-axis will be minutes

# TODO: save in a png, send back to client