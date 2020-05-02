from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = "Home - Post a picth and review others!"
    return render_template('index.html',title = title)

@app.route('/profile/<user>')
def profile(user):

    '''
    View profile page function that returns the profile page and its pitches
    '''
    return render_template('profile.html',id = user)
