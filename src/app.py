from flask import Flask
from flask_cors import CORS

from routes._Routes import Routes
from config.initialize_db import initialize_database

def main():
     app = Flask(__name__)
     CORS(
          app, resources={r"/api/*": {"origins": "*"}}, 
          headers=['Content-Type', 'Authorization'],
          methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
          supports_credentials=True
          )
     
     initialize_database(app=app)

     routes = Routes(app) 
     routes.start_routes()

     app.run(debug=True, port=6587)

if __name__ == "__main__":
     main()