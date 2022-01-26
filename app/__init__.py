from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask_login import LoginManager
from flask_redis import FlaskRedis

from config import ADDRESS, API_ETHERSCAN, ALCHEMY, API_COINGECKO, API_LIQUIDITYFOLIO

# Globally accessible libraries
oracle_configs = {'API_ETHERSCAN': API_ETHERSCAN,
                    'API_COINGECKO': API_COINGECKO,
                    'API_LIQUIDITYFOLIO': API_LIQUIDITYFOLIO,
                    'ALCHEMY': ALCHEMY,
                    'ADDRESS': ADDRESS}
db = SQLAlchemy()
r = FlaskRedis()
migrate = Migrate()
# login_manager = LoginManager()

def init_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.DevConfig')

    # Initialize Plugins
    db.init_app(app)
    r.init_app(app)
    migrate.init_app(app, db)
    # login_manager.init_app(app)

    with app.app_context():
        # Include local applications routing
        # from .authentication.home.routes import home_bp
        # from .authentication.auth.routes import auth_bp
        # from .authentication.user.routes import user_bp
        #
        from .basic.address.routes import address_bp
        from .basic.contract.routes import contract_bp
        from .basic.token.routes import token_bp
        #
        from .deep.transfer.routes import transfer_bp
        from .deep.transaction.routes import transaction_bp
        #
        from .curve.dashboard.routes import curve_dashboard_bp

        ## Including static asset handling
            ### ???
        # from .api import routes
        # from .assets import compile_static_assets

        # Register Blueprints
        # app.register_blueprint(curve_contracts_bp)
        app.register_blueprint(address_bp, url_prefix='/address')
        app.register_blueprint(contract_bp, url_prefix='/contract')
        app.register_blueprint(token_bp, url_prefix='/token')
        #
        app.register_blueprint(transfer_bp, url_prefix='/transfer')
        app.register_blueprint(transaction_bp, url_prefix='/transaction')
        #
        app.register_blueprint(curve_dashboard_bp, url_prefix='/curve_dashboard')

        # Create Database Models
        db.create_all()

        # Compile static assets
        # compile_static_assets(assets)  # Execute logic

        return app
