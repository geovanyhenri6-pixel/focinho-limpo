from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    WHATSAPP_NUMERO = os.environ.get("WHATSAPP_NUMERO")