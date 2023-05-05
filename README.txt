Road Trip Planner
EE 250 Final Semester Project

Team Members
- Jacob Damasco
- Kobe Kodachi

Demo Video
https://drive.google.com/file/d/1JHCX-D26HXODESi_BhsaGaJjbxynHBEt/view

## Instructions
Note: For security purposes, we hid our API key and did not publish it to the repo. You will need your own API key for this to run. Go to the HERE Traffic API in order to get an API key. Once you have an API key, follow the instructions below.

1. Clone the Github repo.
2. Create a file called config.py and enter your API key in the following format:
api_key = "{api key goes here}".
3. Open up 2 terminals. One will run the traffic_client.py file and the other will run the traffic_server.py file.
4. In one of the terminals, SSH into the Raspberry Pi.
5. In the other terminal, run the following command: scp ./traffic_server.py pi@address:
6. In the terminal where you SSHed in, run python3 traffic_server.py.
7. Then, in the other non-SSHed terminal, run python3 traffic_client.py.
8. Input the coordinates of your start and end location, and wait for a bar graph to pop up.

## External Libraries
-  HERE Traffic API (https://developer.here.com/documentation/routing-api/dev_guide/index.html)
- Flask
- PIL (Python Imaging Library)
- PathLIB
- Plotly