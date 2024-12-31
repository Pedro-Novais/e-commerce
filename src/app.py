from flask import Flask
from flask_cors import CORS

from routes._Routes import Routes
from config.initialize_db import initialize_database

def main():
     app = Flask(__name__, subdomain_matching=True)

     # app.config['SERVER_NAME'] = 'ngrok-free.app'
     app.config['SERVER_NAME'] = 'example.local:5000'
     app.config['APPLICATION_ROOT'] = '/'

     CORS(
          app, resources={r"/api/*": {"origins": "*"}}, 
          headers=['Content-Type', 'Authorization'],
          methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
          supports_credentials=True
          )
     
     initialize_database(app=app)

     routes = Routes(app) 
     routes.start_routes()

     app.run(debug=True, host="0.0.0.0", port=5000)

if __name__ == "__main__":
     try:
          main()
     
     except Exception as e:
          print("Erro ao inicializar a aplicação, erro: {}".format(e))