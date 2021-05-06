from flask import Flask
from config import Config
from .site.routes import site
from .authentication.routes import auth
from flask_migrate import Migrate
from drone_inventory.models import db as root_db, login_manager


app = Flask(__name__)

app.config.from_object(Config)

app.register_blueprint(site)
app.register_blueprint(auth)

root_db.init_app(app)
migrate = Migrate(app, root_db)

login_manager.init_app(app)
 #Specifyoing a route for non authorized users

from drone_inventory import models