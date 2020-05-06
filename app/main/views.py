from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import CommentForm, UpdateProfile
from flask_login import login_required, current_user
from .. import db
from ..models import User,Pitch,Comment
import markdown2

# Views
@main.route('/')
def index():

    pickup = Pitch.query.filter_by(category = 'pickup').all()
    product = Pitch.query.filter_by(category = 'product').all()
    promotional = Pitch.query.filter_by(category = 'promotional').all()
    interview = Pitch.query.filter_by(category = 'interview').all()
    title = 'Home - Welcome to the Pitches'
    return render_template('index.html', title = title,pickup = pickup,product = product, pitches = pitches,promotional= promotional ,interview = interview)

@main.route('/create_new', methods = ['POST','GET'])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        category = form.category.data
        user_id = current_user
        new_pitch_object = Pitch(post=post,user_id=current_user._get_current_object().id,category=category,title=title)
        new_pitch_object.save_p()
        return redirect(url_for('main.index'))

    return render_template('create_pitch.html', form = form)


@main.route('/user/<user_id>')
def user(user_id):

    '''
    View pitch page function that returns the pitch details page and its data
    '''
    return render_template('user.html',id = user_id)


@main.route('/pitch/comment/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_comment(id):
    form = CommentForm()
    pitch = get_pitch(id)
    if form.validate_on_submit():
        title = form.title.data
        comment = form.comment.data

        new_comment = Comment(pitch_id=pitch.id, pitch_title = title, pitch_comment = comment, user = current_user)

        new_comment.save_comment()
        return redirect(url_for('.pitch', id = pitch.id))
    title = f'{pitch.title} comment'


    return render_template('comment.html', title = title, comment_form = form, pitch = pitch)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/comment/<int:id>')
def single_comment(id):
    comment=Comment.query.get(id)
    if comment is None:
        abort(404)
    format_comment = markdown2.markdown(comment.pitch_comment,extras=["code-friendly", "fenced-code-blocks"])
    return render_template('comment.html',comment = comment,format_comment=format_comment)
