# ALCHEMY = "https://eth-mainnet.alchemyapi.io/v2/fP_VKPzAULF28EZRrtw5zR7NF8X4k3wI"
# ALCHEMY_WS ="'wss://eth-mainnet.alchemyapi.io/v2/fP_VKPzAULF28EZRrtw5zR7NF8X4k3wI'"
# API_ETHERSCAN = "E9V2IBKAHGCREJJ3RYAC5FRHSDI8MPDB5P"
#
#
# ADDRESSES = ["0x17e33637f6B64E9082Ea499481b6e6EbAE7EEA23"]

ADDRESS = ""
API_ETHERSCAN = "<API_ETHERSCAN>"
ALCHEMY = "https://eth-mainnet.alchemyapi.io/v2/<ALCHEMYKEY>"
FLASK_SECRET_KEY = "<password>"
PROVIDER = "wss://eth-mainnet.ws.alchemyapi.io/v2/<ALCHEMYKEY>"
DATABASE_NAME = "curve_wars"
API_COINGECKO = "<API-COINGECKO>"
API_LIQUIDITYFOLIO = "<API_LIQUIDITYFOLIO>"

PROD_DB_CREDS = {
    'username': '<username>',
    'password': '<password>',
    'hostname': '<url>',
    'databasename': DATABASE_NAME
    }

PROD_DATABASE_URI = "postgresql://super:{password}@{hostname}/{databasename}".format(
    username= PROD_DB_CREDS['username'],
    password= PROD_DB_CREDS['password'],
    hostname= PROD_DB_CREDS['hostname'],
    databasename= PROD_DB_CREDS['databasename'],
)

DEV_DB_CREDS = {
    'username': '<username>',
    'password': '<password>',
    'hostname': 'localhost:<port>',
    'databasename': DATABASE_NAME
    }

DEV_DATABASE_URI = "postgresql://super:{password}@{hostname}/{databasename}".format(
    username= DEV_DB_CREDS['username'],
    password= DEV_DB_CREDS['password'],
    hostname= DEV_DB_CREDS['hostname'],
    databasename= DEV_DB_CREDS['databasename'],
)
#
# class Config():
#     self.SQLALCHEMY_TRACK_MODIFICATIONS = False
#     self.SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
#     self.SQLALCHEMY_POOL_RECYCLE = 299
#     self.SECRET_KEY = FLASK_SECRET_KEY


"""Flask configuration variables."""
from os import environ, path
# from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
# load_dotenv(path.join(basedir, '.env'))

# class Config:
#     # General Config
#     SECRET_KEY = environ.get('SECRET_KEY')
#     FLASK_APP = environ.get('FLASK_APP')
#     FLASK_ENV = environ.get('FLASK_ENV')
#
#     # Flask-Assets
#     LESS_BIN = environ.get('LESS_BIN')
#     ASSETS_DEBUG = environ.get('ASSETS_DEBUG')
#     LESS_RUN_IN_DEBUG = environ.get('LESS_RUN_IN_DEBUG')
#
#     # Static Assets
#     STATIC_FOLDER = 'static'
#     TEMPLATES_FOLDER = 'templates'
#     COMPRESSOR_DEBUG = environ.get('COMPRESSOR_DEBUG')
#
#     # Flask-SQLAlchemy
#     SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
#     SQLALCHEMY_ECHO = False
#     SQLALCHEMY_TRACK_MODIFICATIONS = False


class Config:
    """Base config."""
    SECRET_KEY = FLASK_SECRET_KEY

    # Flask-Assets
    LESS_BIN = environ.get('LESS_BIN')
    ASSETS_DEBUG = environ.get('ASSETS_DEBUG')
    LESS_RUN_IN_DEBUG = environ.get('LESS_RUN_IN_DEBUG')

    # Static Assets
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    COMPRESSOR_DEBUG = environ.get('COMPRESSOR_DEBUG')


class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False

    # Flask-SQLAlchemy
    SQLALCHEMY_DATABASE_URI = PROD_DATABASE_URI
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True

    # Flask-SQLAlchemy
    SQLALCHEMY_DATABASE_URI = DEV_DATABASE_URI
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
