from flask import Blueprint, blueprints
from .UserRoute import user_route

class Routes:
    def __init__(self, app):
        self.app = app

    def start_routes(self):
        self.app.register_blueprint(user_route, url_prefix='/api/user')