from flask import Flask
from config import Config
from routes.site import site

app = Flask(__name__)
app.register_blueprint(site)