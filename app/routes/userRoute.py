from flask import flash, render_template, request, redirect, url_for, Blueprint
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash
from app.main.models.user import User
from app.main.auth.userauth import login_auth, signup_auth
from app.main.services.userservices import user_service
from app.main.db import session




user_bl = Blueprint('user', __name__)




@user_bl.get('/signup')
def signup():
    return render_template('signup.html')



@user_bl.post('/signup')
def create_user():

    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm')

    user_auth = signup_auth()
        

    if user_auth.check_email(email) is not True:

        if user_auth.check_username(username) is not True:
            
            if user_auth.check_password(password, confirm_password) == True:

                if len(password) > 5 :   

                    password_hash = generate_password_hash(password, 'sha256', 16)

                
                    new_user = User(first_name=first_name, username=username, last_name=last_name, email=email, password_hash=password_hash)
                    session.add(new_user)
                    session.commit()

                    return redirect(url_for('user.login'))

                flash('Your password should have more the 5 characters')
                return render_template("signup.html")
                
            flash('Passwords do not match')
            return render_template("signup.html")

        flash('Username already exits')
        return render_template("signup.html")


    flash('Email already exits')
    return render_template("signup.html")



@user_bl.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('signin.html')


@user_bl.post('/login/')
def signin_user():

    
    email = request.form.get('email')
    password = request.form.get('password')

    user = session.query(User).filter_by(email=email).first()

        
    user_auth = login_auth()

    if user_auth.confirm_user(email, password) is True:
            
           
        login_user(user)
        return redirect(url_for('post.home'))

    flash('Your credentials do not match')
    return redirect(url_for('.login'))


@user_bl.get('/profile/update')
def get_user():

    return render_template('userupdate.html')


@user_bl.post('/profile/update/<username>')
def update_user(username):

    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    new_username = request.form.get('username')
    email = request.form.get('email')
    # user = session.query(User).get(user_id)

    user_to_update = user_service()
    user_to_update.update_user(username, first_name, last_name, new_username, email)

    
    return redirect(url_for('post.update_post_username', username=username, new_username=new_username))


@user_bl.get('/profile/change_password')
def change_pass():
    return render_template('changepassword.html')


@user_bl.post('/change_password/<username>')
def change_password(username):

    old_password = request.form.get('old_password')
    confirm_password = request.form.get('confirm')
    new_password = request.form.get('new_password')

    user_auth = signup_auth()

    if user_auth.check_password(old_password, confirm_password) == True:
        password_to_change = user_service()

        if password_to_change.update_password(username, old_password, new_password) == True:

            return redirect(url_for('post.get_post_by_user', username=username))

        flash('An error has occured')    
        return render_template('changepassword.html')

    flash('your credentials do not match')
    return render_template('changepassword.html')

    
@user_bl.get('/logout')
def logout():
    logout_user()
    return redirect(url_for('post.home'))