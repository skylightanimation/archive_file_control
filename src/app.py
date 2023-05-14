import os
from flask import Flask,  request, url_for, redirect, flash #, render_template, session
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
# from flask_swagger_ui import get_swaggerui_blueprint


from marshmallow import Schema, fields 
from sqlalchemy.sql import func
from systems import database, security


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = database.Database._connection
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = security.BlackJack._secret
db = SQLAlchemy(app)
ma = Marshmallow(app)


from controllers import projectionController
from controllers import animeStatusController


@app.route('/root', methods=['GET'])
def root():
	return 'try!'

if __name__ == '__main__':
    app.run(host="localhost", port=5011, debug=True)
    
	# port = int(os.environ.get('PORT', 5011))
	# app.run(debug=True, port=port)