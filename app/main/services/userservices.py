from app.main.models.user import User
from werkzeug.security import generate_password_hash, check_password_hash
from app.main.db import session

class user_service():

    def update_user(self, username: str, fname: str, lname: str, new_username: str, email: str, display_pic: str, background_pic: str):
        
        user_to_update = session.query(User).filter_by(username=username).first()
        
        if display_pic != '':
            user_to_update.display_pic = display_pic
        if background_pic != '':
            user_to_update.background_pic = background_pic

        user_to_update.first_name = fname
        user_to_update.last_name = lname
        user_to_update.username = new_username
        user_to_update.email = email

        session.commit()


    def update_password(self, username: str, old_password: str, new_password: str):
        
        user_to_update = session.query(User).filter_by(username=username).first()

        if user_to_update and check_password_hash(user_to_update.password_hash, old_password):
            new_password_hash = generate_password_hash(new_password, 'sha256', 16)

            user_to_update.password_hash = new_password_hash
                        
            session.commit()

            return True

        # flash('wrong old pass')
        return False         