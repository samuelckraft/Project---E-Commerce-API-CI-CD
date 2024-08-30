from password import password

class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://root:{password}@localhost/advanced_flask_api'
    CACHE_TYPE = 'SimpleCache'
    DEBUG = True