from werkzeug.security import check_password_hash
from app.main.models.user import User
from app.main.db import session


class signup_auth():

        def check_email(self, email: str):
        
            email_exits = session.query(User).filter_by(email=email).first()

            if email_exits:
                return True
                
        def check_password(self, password: str, confirm_password: str):
                if password == confirm_password:
                    return True

                return False

        def check_username(self, username: str):
                
            username_exits = session.query(User).filter_by(username=username).first()

            if username_exits:
                return True

                    
class login_auth():       
                        
        def confirm_user(self, email: str, password: str):
            
            user = session.query(User).filter_by(email=email).first()
            return user and check_password_hash(user.password_hash, password)
              

