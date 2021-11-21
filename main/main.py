import requests
from dataclasses import dataclass
from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
from producer import publish

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@db/main'
CORS(app)

db = SQLAlchemy(app)


@dataclass
class Product(db.Model):
    id: int
    title: str
    image: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))


@dataclass
class ProductUser(db.Model):
    id: int
    user_id: int
    product_id: int

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    UniqueConstraint('user_id', 'product_id', name='user_product_unique')


@app.route('/api/products')
def index():
    return jsonify(Product.query.all())


@app.route('/api/products/like', methods=['POST'])
def like():
    data = request.json

    user_id = data.get('user_id')
    product_id = data.get('product_id')

    response = requests.get(
        f'http://docker.for.mac.localhost:8000/api/users/{user_id}')
    response_data = response.json()

    try:
        user_id = response_data.get('id')
        productUser = ProductUser(
            user_id=user_id,
            product_id=product_id
        )
        db.session.add(productUser)
        db.session.commit()

        publish('product_liked', product_id)
    except Exception:
        abort(400, 'You already liked this product')

    return jsonify({'message': 'success'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
