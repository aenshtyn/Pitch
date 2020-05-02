import urllib.request,json
from .models import Pitch

# Getting api key
api_key = None
# Getting the pitch base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['PITCH_API_KEY']
    base_url = app.config['PITCH_API_BASE_URL']
