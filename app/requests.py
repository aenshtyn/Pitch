import urllib.request,json
from .models import Pitch

base_url = None

def configure_request(app):

    base_url = app.config['SQLALCHEMY_DATABASE_URI']

def get_pitches(category):

    return pitch_results

def process_results(pitch_list):

    pitch_results = []
    for pitch_item in pitch_list:
        id = pitch_item.get('id')
        category  = pitch_item.get('category')
        title = pitch_item.get('title')
        content = pitch_item.get('content')
        author = pitch_item.get('author')


    return pitch_results
