from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

order_put_args = reqparse.RequestParser()
order_put_args.add_argument("orderID", type=int, help="Name of the video is required", required=True)
order_put_args.add_argument("meal", type=str, help="Name of the meal is required", required=True)
order_put_args.add_argument("main", type=int, help="Name of the main entree is required", required=True)
order_put_args.add_argument("side", type=int, help="Name of the side entree is required", required=True)
order_put_args.add_argument("drink", type=int, help="Name of the drink is allowed")
order_put_args.add_argument("dessert", type=int, help="Name of the dessert is required")

orders = {}

def abort_if_order_doesnt_exist(order_id):
    if order_id not in orders:
        abort(404, message = "Order ID is not valid...")

def abort_if_order_exists(order_id):
    if order_id in orders:
        abort(409, message = "Order ID is already taken...")

class Order(Resource):
    def get(self, order_id):
        abort_if_order_doesnt_exist(order_id)
        return orders[order_id]

    def put(self, order_id):
        args = order_put_args.parse_args(order_id)
        orders[order_id] = args
        return orders[order_id], 201

api.add_resource(Order, "/Order/<int:order_id>")

if __name__ == '__main__':
    app.run(debug=True)