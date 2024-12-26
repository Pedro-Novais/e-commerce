from flask import Blueprint, blueprints
from .UserRoute import user_route
from .ProductsRoute import product_route
from .OrdersRoute import order_route

class Routes:
    def __init__(self, app):
        self.app = app

    def start_routes(self):
        self.app.register_blueprint(user_route, url_prefix='/api/user')
        self.app.register_blueprint(product_route, url_prefix='/api/product')
        self.app.register_blueprint(order_route, url_prefix='/api/order')