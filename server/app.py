#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate
from models import db, Bakery, BakedGood
from sqlalchemy import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@app.route('/bakeries')
def bakeries():
    bakeries = []
    for bakery in Bakery.query.all():
        bakery_dict = {
            'id': bakery.id,
            'name': bakery.name,
            'created_at': bakery.created_at,
            'updated_at': bakery.updated_at,
        }
        bakeries.append(bakery_dict)
    
    response = make_response(
        bakeries,
        200,
        {'Content-Type': 'application/json'}
    )
    return response

@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    selected_bakery = Bakery.query.filter(Bakery.id == id).first()
    selected_bakery = selected_bakery.to_dict()
    # if selected_bakery:
    #     bakery_dict = {
    #         "id": selected_bakery.id,
    #         "name": selected_bakery.name,
    #         "created_at": selected_bakery.created_at,
    #         "updated_at": selected_bakery.updated_at,
    #     }
    response = make_response(
        jsonify(selected_bakery),
        200,
        {'Content-Type': 'application/json'}
    )
    return response

@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    pastries = []
    for pastry in BakedGood.query.order_by(BakedGood.price).all():
        pastry_dict = {
            "id": pastry.id,
            "name": pastry.name,
            "price": pastry.price,
            "created_at": pastry.created_at,
            "updated_at": pastry.updated_at,
        }
        pastries.append(pastry_dict)
    response = make_response(
        pastries,
        200,
        {"Content-Type":"application/json"}
    )
    return response
@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    # selected_pastry = BakedGood.query.group_by(BakedGood.price).having(func.max(BakedGood.price)).first()
    selected_pastry = BakedGood.query.order_by(BakedGood.price.desc()).first()
    selected_pastry = selected_pastry.to_dict()
    print(jsonify(selected_pastry))
    response = make_response(
        jsonify(selected_pastry),
        200,
    )
    return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)
