from flask import render_template
from app import app
from .models import comments
from .forms import CommentForm

Comment = comment.Comment

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


@app.route('/pitch/comment/new/<int:id>', methods = ['GET', 'POST'])
def new_comment(id):
    form = CommentForm()
    pitch = get_pitch(id)

    if form.validate_on_submit():
        name = form.name.data
        comment = form.comment.data
        new_comment = Comment(pitch.id,name,comment)
        new_comment.save_comment()
        return redirect(url_for('pitch',id = pitch.id ))

    name = f'{pitch.name} comment'
    return render_template('new_comment.html', name = name, comment_form = form, pitch = pitch)
