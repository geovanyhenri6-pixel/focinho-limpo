from dotenv import load_dotenv
import os

load_dotenv()
class Config:
    chave= os.environ.get("SECRET_KEY")
    numero_zap= os.environ.get("WHATSAPP_NUMERO")
    if chave and numero_zap:
        SECRET_KEY= os.environ.get("SECRET_KEY")
        WHATSAPP_NUMERO= os.environ.get("WHATSAPP_NUMERO")
    else:
        if not chave:
            raise RuntimeError("A variável de ambiente 'SECRET_KEY' não foi definida. O aplicativo não pode ser iniciado por motivos de segurança.")
        elif not numero_zap:
            raise RuntimeError("A variável de ambiente 'WHATSAPP_NUMERO' não foi definida. Para evitar erros o aplicativo não será iniciado.")