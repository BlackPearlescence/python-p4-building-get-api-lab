from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.dialects.sqlite import DATETIME

db = SQLAlchemy()
dt = DATETIME()
class Bakery(db.Model, SerializerMixin):
    __tablename__ = 'bakery'

    serialize_rules = ("baked_goods.bakery",)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    created_at = db.Column(db.String)
    updated_at = db.Column(db.String)

    baked_goods = db.relationship('BakedGood', back_populates='bakery', lazy=True)

class BakedGood(db.Model, SerializerMixin):
    __tablename__ = 'baked_goods'

    serialize_rules = ("-bakery.baked_goods",)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Float)
    created_at = db.Column(db.String)
    updated_at = db.Column(db.String)
    bakery_id = db.Column(db.Integer, db.ForeignKey('bakery.id'))


    bakery = db.relationship('Bakery', back_populates='baked_goods')



