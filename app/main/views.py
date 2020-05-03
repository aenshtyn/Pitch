from flask import render_template,request,redirect,url_for
from . import main
from ..models import Comment
from .forms import CommentForm
from ..requests import get_pitches,get_pitch,search_pitch
from flask_login import login_required


Comment = comment.Comment

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = "Home - Post a picth and review others!"
    return render_template('index.html',title = title)

@main.route('/pitch/<id>')
def pitch(id):

    '''
    View profile page function that returns the profile page and its pitches
    '''
    pitch = get_pitch(id)
    title = f'{pitch.title}'
    comments = Comment.get_comment(pitch.id)

    return render_template('pitch.html', title = title, pitch = pitch, comments = comments )


@main.route('/pitch/comment/new/<int:id>', methods = ['GET', 'POST'])
@login_required
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
