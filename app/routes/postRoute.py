
from flask import flash, render_template, request, redirect, url_for, Blueprint
from flask_login import current_user, login_required 
from app.main.models.post import Post
from app.main.models.user import User
from app.main.services.postservices import post_service
from app.main.db import session

# from app import app

post_bl = Blueprint('post', __name__)


@post_bl.get('/')
def home():
    return redirect(url_for('.get_all_posts'))


@post_bl.route('/home', methods=['GET', 'POST'])
def get_all_posts():

    posts = session.query(Post).order_by(Post.date_updated.desc()).all()

    trend_post = session.query(Post).order_by(Post.no_of_views.desc()).limit(5).all()
    
    if request.method == 'GET':
        if posts:
            return render_template('index.html', posts=posts, trend=trend_post)
        return render_template('index.html')

    elif request.method == 'POST':
        search_criteria = request.form.get('search')
        search_for = request.form.get('search_post')

        
        search = "%{}%".format(search_for)
       
        if search:
            if search_criteria == 'search_title':
                result = session.query(Post).filter(Post.title.ilike(search)).order_by(Post.date_updated.desc()).all()

                # return render_template('index.html', posts=posts, result=result)

            else:
                        # search_criteria == 'search_blogger'
                result = session.query(Post).filter(Post.username.ilike(search)).order_by(Post.date_updated.desc()).all()
                # return render_template('index.html', posts=posts, result=result)

            if result:
                return render_template('index.html', posts=posts, result=result)

            flash('No post found')
            return render_template('index.html', posts=posts)

        return render_template('index.html', posts=posts)

    return render_template('index.html')



@post_bl.get('/post/<int:post_id>')
def get_post_by_id(post_id):

    post = session.query(Post).filter_by(id=post_id)

    return render_template('postupdate.html', post=post)


@post_bl.route('/profile/<username>', methods=['GET', 'POST'])
def get_post_by_user(username):

    user_posts = session.query(Post).filter_by(username=username).order_by(Post.date_updated.desc()).all()

    blogger = session.query(User).filter_by(username=username).first()

    trend_post = session.query(Post).order_by(Post.no_of_views.desc()).limit(5).all()
    
    if request.method == 'GET':
        if user_posts:
            return render_template('profile.html', user_posts=user_posts, blogger=blogger, trend=trend_post)
        
        elif trend_post:    
            return render_template('profile.html', blogger=blogger, trend=trend_post)
        else:
            return render_template('profile.html', blogger=blogger)

    elif request.method == 'POST':
        search_criteria = request.form.get('search')
        search_for = request.form.get('search_post')

        
        search = "%{}%".format(search_for)
       
        if search:
            if search_criteria == 'search_title':
                result = session.query(Post).filter(Post.title.ilike(search)).order_by(Post.date_updated.desc()).all()

                # return render_template('profile.html', user_posts=user_posts, blogger=blogger, result=result)

            else:
                        # search_criteria == 'search_blogger'
                result = session.query(Post).filter(Post.username.ilike(search)).order_by(Post.date_updated.desc()).all()
                # return render_template('profile.html', user_posts=user_posts, blogger=blogger, result=result)
        
            if result:
                return render_template('profile.html', user_posts=user_posts, blogger=blogger, result=result)
                
            flash('No post was found')
            return render_template('profile.html', user_posts=user_posts, blogger=blogger)

        return render_template('profile.html', user_posts=user_posts, blogger=blogger)
            
    return render_template('profile.html')

   

@post_bl.get('/post')
def post():

    if current_user.is_authenticated:
        return render_template('post.html')  
    
    return redirect(url_for('user.login'))



@post_bl.post('/post/<username>')
@login_required
def add_post(username):

    # if request.method == 'POST':
    title = request.form.get('title')
    content = request.form.get('content')

    new_post = post_service()
    new_post.create_post(title, content, username)
        # new_post = Post(title=title, content=content, user_id=user_id)
        
        
    return redirect(url_for('post.home'))

    # return redirect(url_for('add_post', user_id=user_id))


@post_bl.route('/post/update/<int:post_id>', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    post = session.query(Post).get(post_id)

    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')

        updated_post = post_service()
        updated_post.update_post(title, content, post_id)
        # new_post = Post(title=title, content=content, user_id=user_id)
        
        
        return redirect(url_for('.get_post_by_user', username=post.username))
        # return render_template('userupdate.html', posts=post_to_update)

    return redirect(url_for('.edit_post', post_id=post_id))


@post_bl.get('/<username>/<new_username>')
@login_required
def update_post_username(username, new_username):

    user_posts = session.query(Post).filter_by(username=username).all()
    
    if user_posts:

        for post in user_posts:
            post.username = new_username

        session.commit()

        return redirect(url_for('.get_post_by_user', username=new_username))

    return redirect(url_for('.get_post_by_user', username=new_username))


@post_bl.get('/post/delete/<int:post_id>')
@login_required
def delete_post(post_id):
    post = session.query(Post).get(post_id)
    post_to_delete = post_service()
    post_to_delete.delete_post(post_id)

    return redirect(url_for('.get_post_by_user', username=post.username))
    

@post_bl.get('/post/<int:post_id>/')
def read_count(post_id):
    post = session.query(Post).get(post_id)

    post.no_of_views = post.no_of_views + 1

    session.commit()

    return render_template('readpost.html', read_post=post)