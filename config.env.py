import os

# Flask config
DEBUG=False
IP=os.environ.get('BINGEBOARD_IP', '0.0.0.0')
PORT=int(os.environ.get('BINGEBOARD_PORT', '8080'))
SERVER_NAME = os.environ.get('BINGEBOARD_SERVER_NAME', 'binge.csh.rit.edu')
SECRET_KEY = os.environ.get('BINGEBOARD_SECRET_KEY', '')

SQLALCHEMY_DATABASE_URI = os.environ.get(
    'BINGEBOARD_DATABASE_URI',
    'sqlite:///{}'.format(os.path.join(os.getcwd(), 'data.db')))
SQLALCHEMY_TRACK_MODIFICATIONS = False
