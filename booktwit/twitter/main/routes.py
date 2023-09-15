from flask import render_template, request, Blueprint
from twitter.models import Post, Announcement
from twitter import db
import datetime

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)


@main.route("/about")
def about():
    return render_template('about.html', title='About')

@main.route("/calendar")
def calendar():
    return render_template('calendar.html', title='Calendar')


@main.route("/announcements")
def announcements():
    page = request.args.get('page', 1, type=int)
    announcements = Announcement.query.order_by(Announcement.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('announcements.html', title='Announcements', announcements=announcements)

#announcements must manually be added by database queries.

#in order to create new announcement, run python3 then follow these terminal commands:
#from twitter import create_app
#app = create_app()
#app.app_context().push()
#from twitter import db
#from twitter.models import Announcement
#announcement_1 = Announcement(title='Upcoming Book Reading Event!', date_posted= datetime.date(2022, 12, 25), content='Book of the month is This is How you Lose the Time War!')
#db.session.add(announcement_1)
#db.session.commit()