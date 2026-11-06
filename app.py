from flask import Flask, current_app
from config import Config
from routes.site import site

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(site)

@app.context_processor
def inject_whatsapp():
    whatsapp_numero = current_app.config['WHATSAPP_NUMERO']
    return {'whatsapp_numero': whatsapp_numero}