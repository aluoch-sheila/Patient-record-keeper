from flask_login import current_user, login_required

from . import main
from .. import db, photos
from ..email import mail_message
from ..models import Comment, Post, Subscriber, User
from .forms import CommentForm, PostForm, SubscribeForm, UpdateProfile


@main.route('/')
def index():
  
  title = 'Home - Welcome to Patients record keeper'
  Records = Record.get_Record()

  return render_template('index.html', title = title, Records = Records)


@main.route('/Record/new', methods = ['GET','POST']) 
@login_required
def new_Record():
  form = RForecordm()

  if form.validate_on_submit():
    title = form.title.data
    Record = form.Record.data
    new_Record = Record(Record_title = title, Record_text = Record user=current_user )
    new_Record.save_R(ecord)

    users = Subscriber.query.all()
    for user in users:
        print(user.email)
        mail_message("New Record on the patient record keeper","email/sub_alert",user.email,user=user)  

    return redirect(url_for('.index'))

  title = 'New Record'
  return render_template('new_Records.html', title= title, form= form)


@main.route('/Record/comments/new/<int:id>', methods = ['GET', 'POST'])
def new_comment(id):
  form = CommentForm()
  print(id)

  if form.validate_on_submit():
    post_id = id
    comment = form.comment.data
    print(comment)
    new_comment = Comment(comment_text= comment,post_id= post_id)
    new_comment.save_comment()
    return redirect(url_for('.view_Record',id = id))

  title = 'New Comment'
  return render_template('new_comments.html', title= title, form= form)


@main.route('/Record/comment/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_comment(id):
    comment = Comment.query.filter_by(id=id).first()
    Record= comment.Record_id
    print(Record_id)
    Comment.delete_comment(id)
    print(Record_id)
    return redirect(url_for('.view_post',id=Record_id))


@main.route('/Record/view/<int:id>', methods=['GET', 'POST'])
def save_Record(id):
    test = id
    print(test)
    Record= Record.query.filter_by(id=id).first()
    print(Record.Record.txt)
    comments = Comment.get_comments(id)
    return render_template('view.html',Record=Record, comments=comments, id=id)


@main.route('/Record/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_Record(id):  
    Record.delete_Record(id)

    return redirect(url_for('.index'))


@main.route('/Record/upedate/<int:id>', methods=['GET', 'POST'])
@login_required
def update_Record(id):
    Record = Record.get_Record(id) 
    form = RecordForm()
  
    if form.validate_on_submit():
        Record.post_title=form.title.data
        Record.Record.txt=form.Record.data
        Record.save_Record()

        return redirect(url_for('.index'))

    title = 'Update Post'
    return render_template('new_posts.html', title= title, form= form)


@main.route('/subscribe',methods = ["GET","POST"])
def subscribe():
    form = SubscribeForm()
    if form.validate_on_submit():
        user = Subscriber(email = form.email.data, username = form.username.data)
        db.session.add(user)
        db.session.commit()

        mail_message("Welcome To patient record keeper","email/sub",user.email,user=user)

        return redirect(url_for('.index'))
    title = "New Subscription"
    return render_template('subscribe.html',form = form, title= title)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)
    print(user.id)
    posts = Post.query.filter_by(user_id=user.id).order_by(Post.post_time.desc()).all()

    return render_template('profile/profile.html',user = user,posts=posts)


@main.route('/user/<uname>/update', methods=['GET', 'POST'])
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()
    
    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname = user.username))

    return render_template('profile/update.html',form = form)
    

@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))
