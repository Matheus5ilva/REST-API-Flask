from flask import Flask, render_template, request, redirect, jsonify, Response, make_response
from template import repositorio
from restApi import ws

app = Flask(__name__)

app.register_blueprint(repositorio)
app.register_blueprint(ws)

app.run(debug=True)