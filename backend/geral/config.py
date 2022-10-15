from flask import Flask, jsonify, request, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import date
from flask_ipban import IpBan
from flask_gzipbomb import GzipBombResponse
from flask_antijs import AntiJs
import os
app = Flask(__name__)
CORS(app)
AntiJs(app)
caminho = os.path.dirname(os.path.abspath(__file__)) 
arquivobd = os.path.join(caminho, "pessoas.db")
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{arquivobd}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)
ip_ban = IpBan(ban_seconds=200000)
ip_ban.init_app(app)
