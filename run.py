from flask import Flask

from app.main.db import Base, engine
from dotenv import load_dotenv
from flask_login import LoginManager
from app.main.models.user import User

from app.main.db import session


from app.routes.postRoute import post_bl
from app.routes.userRoute import user_bl


load_dotenv()

UPLOAD_FOLDER = 'static/images/'

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["SECRET_KEY"] = '6ead16367a858a8ca2ed8c2e'


app.register_blueprint(post_bl)
app.register_blueprint(user_bl)

Base.metadata.create_all(bind=engine)


login_manager = LoginManager(app)


@login_manager.user_loader
def user_loader(id):
    return session.query(User).get(id)

