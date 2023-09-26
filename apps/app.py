from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from pathlib import Path
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
csrf = CSRFProtect()
def create_app():
    # Flaskインスタンス生成
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY="2AZSMss3p5QPbcY2hBsj",
        SQLALCHEMY_DATABASE_URI=
          f"sqlite:///{Path(__file__).parent / 'local.sqlite'}",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SQLALCHEMY_ECHO=True,
        WTF_CSRF_SECRET_KEY="gffgskgangkgnskg",
    )
    csrf.init_app(app)

    # SQLAlchemyとアプリを連携する
    db.init_app(app)
    # Migrateとアプリを連携する
    Migrate(app, db)

    from apps.crud import views as crud_views
    app.register_blueprint(crud_views.crud, url_prefix="/crud")
    return app