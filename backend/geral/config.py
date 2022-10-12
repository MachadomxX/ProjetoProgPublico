from flask import Flask, jsonify, request, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import date
import os
app = Flask(__name__)
CORS(app)
caminho = os.path.dirname(os.path.abspath(__file__)) 
arquivobd = os.path.join(caminho, "pessoas.db")
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{arquivobd}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)
