from flask import Flask
from app.routes import home, dashboard

def create_app(test_config=None):
    app = Flask(__name__, static_url_path='/')
    app.url_map.strict_slashes = False
    app.config.from_mapping(
        SECRET_KEY='super_secret_key'
    )

    from app.routes import home
    app.register_blueprint(home)


    from app.routes import dashboard
    app.register_blueprint(dashboard)

    @app.route('/hello')
    def hello():
        return 'hello world'

    return app
