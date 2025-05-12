class Config:
    # SQLALCHEMY_DATABASE_URI = (
    #     f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@"
    #     f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    # )
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@db/testdb'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SWAGGER = {
        'title': 'Flask REST API',
        'uiversion': 3
    }
