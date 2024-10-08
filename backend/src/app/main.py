from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_restx import Api

from ..databases import db
from .models import Employee, Client, Equipment, Rental, BlacklistToken, BlacklistToken as blacklist_tokens_table
from .routes import auth_namespace, clients_namespace, employees_namespace, equipments_namespace, rentals_namespace


def create_app(config):
    """
    Create a Flask application instance.

    This function handles the setup and initialization of major components for the app, including:

    - Flask: The core framework.
    - CORS (Cross-Origin Resource Sharing): Handles potential issues from making
      requests to the server from different origins.
    - Flask-SQLAlchemy: Initializes the database component.
    - Flask-Migrate: Handles database migrations.
    - JWTManager: Handles JSON Web Tokens for authentication.
    - Flask-Restx and Namespaces: For easy creation of REST APIs.
    - Shell context: Simplifies shell context for Flask shell.

    :param config: The configuration object for Flask.
    :return: Flask app instance.
    """
    # Create Flask app instance.
    app = Flask(__name__)
    # Load config from config object.
    app.config.from_object(config)

    # Enable CORS for the app.
    CORS(app, supports_credentials=True, resources={r"/*": {"origins": "*"}})
    # CORS(app, supports_credentials=True, origins=['http://localhost:3000'])
    # Initialize SQLAlchemy with app.
    db.init_app(app)
    # Initialize Flask-Migrate for handling migrations.
    Migrate(app, db)
    # Setup the Flask-JWT-Extended extension.
    jwt_manager = JWTManager(app)
    # List all the headers  client might send, including custom ones
    allowed_headers = ['Content-Type', 'Authorization', 'Access-Control-Allow-Origin']



    @jwt_manager.token_in_blocklist_loader
    def check_if_token_in_blacklist(jwt_header, jwt_payload):
        """
        Check if the current JWT token is in the blacklist.

        :param jwt_header: The header of the JWT.
        :param jwt_payload: The payload of the JWT.

        :return: Boolean indicating if the token is blacklisted.
        :rtype: bool
        """
        jti = jwt_payload["jti"]
        token = blacklist_tokens_table.query.filter_by(jti=jti).scalar()

        return token is not None

        # Ensure OPTIONS requests are handled correctly (preflight)
    @app.before_request
    def handle_options_request():
        if request.method == 'OPTIONS':
            return jsonify({'status': 'ok'}), 200

    @app.after_request
    def apply_cors(response):
        response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        response.headers['Access-Control-Allow-Headers'] = ', '.join(allowed_headers)
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS, PUT, DELETE'
        return response

    # Initialize Flask-Restx Api.
    api = Api(app, doc='/docs')
    # Add namespaces.
    # Add namespaces to the API
    api.add_namespace(equipments_namespace, path='/equipments')
    api.add_namespace(auth_namespace, path='/auth')
    api.add_namespace(clients_namespace, path='/clients')
    api.add_namespace(employees_namespace, path='/employees')
    api.add_namespace(rentals_namespace, path='/rentals')

    @app.shell_context_processor
    def make_shell_context():
        """
        Make context for flask shell command.

        :return: dictionary with context data.
        """
        return {"db": db, "Employee": Employee, "Client": Client, "Equipment": Equipment, "Rental": Rental,
                "BlacklistToken": BlacklistToken}

    return app
