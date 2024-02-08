import os
from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from .database import db
from flask_gravatar import Gravatar
from flask_login import LoginManager


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.environ.get("FLASK_KEY")
    ckeditor = CKEditor(app)
    Bootstrap5(app)

    # Create database
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_URI", 'sqlite:///blog.db')
    db.init_app(app)

    from .models import User, BlogPost, Comment

    with app.app_context():
        db.create_all()

    # For adding profile images to the comment section
    gravatar = Gravatar(app,
                        size=100,
                        rating='g',
                        default='retro',
                        force_default=False,
                        force_lower=False,
                        use_ssl=False,
                        base_url=None)

    # Configure Flask-Login
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return db.get_or_404(User, user_id)

    from .auth import auth
    from .views import views

    app.register_blueprint(views)
    app.register_blueprint(auth)

    return app
