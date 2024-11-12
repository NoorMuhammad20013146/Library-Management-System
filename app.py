from flask import Flask, jsonify, request, render_template
from flask_mysqldb import MySQL
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)