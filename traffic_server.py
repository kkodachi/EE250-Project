from typing import Dict, List, Optional
from flask import Flask, request, jsonify, make_response
import pathlib
import json
import plotly.graph_objs as go

app = Flask(__name__)
# path to directory of this file
thisdir = pathlib.Path(__file__).parent.absolute() 

def load_traffic():
    try:
        return json.loads(thisdir.joinpath('traffic_db.json').read_text())
    except FileNotFoundError:
        return []
    
def seconds_to_minutes():
    pass

@app.route('/traffic', methods=['POST'])
def traffic():
    # DONE: get the list of traffic data
    traffic_data_json = request.get_json()
    traffic_data = json.dumps(traffic_data_json)
    traffic_data = json.loads(traffic_data)
    
    # DONE: plot element of each hour in a bar graph with plotly
    # x-axis will be the time (0, 1, 2, ..., 24), y-axis will be minutes
    times = ['12am', '1am', '2am', '3am', '4am', '5am', '6am', '7am', 
             '8am', '9am', '10am', '11am', '12pm', '1pm', '2pm', '3pm', 
             '4pm', '5pm', '6pm', '7pm', '8pm', '9pm', '10pm', '11pm']
    trace = go.Bar(x=times, y=traffic_data)
    layout = go.Layout(
        title='Road Trip Planner: ',
        xaxis=dict(title='Time'),
        yaxis=dict(title='Commute Time (mins)')
    )
    fig = go.Figure(data=[trace], layout=layout)

    # save img
    img_bytes = fig.to_image(format='png')

    # DONE: save in a png, send back to client
    response = make_response(img_bytes)
    response.headers.set('Content-Type', 'image/png')
    response.headers.set('Content-Disposition', 'attachment', filename='roadtrip_planner.png')

    return response

if __name__ == "__main__":
    app.run(host='172.20.10.3',port=5000, debug=True)