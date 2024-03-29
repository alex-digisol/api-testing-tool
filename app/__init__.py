import os
from oauthlib.oauth2 import WebApplicationClient
from flask import Flask,render_template


from .database import init_db
from .auth import GOOGLE_CLIENT_ID


def create_app() -> Flask:
    app = Flask(__name__)
    init_db()
    
    app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(64)
    app.config["google_client"] = WebApplicationClient(GOOGLE_CLIENT_ID)

    # Blueprints
    from .auth import auth
    app.register_blueprint(auth)
        
    from .projects import projects
    app.register_blueprint(projects)

    from .main import main
    app.register_blueprint(main)

    from .static_pages import static_pages
    app.register_blueprint(static_pages)

    @app.errorhandler(404)
    def not_found(e):
        return render_template("404.html")

    @app.errorhandler(500)
    def error(e):
        return render_template("500.html")

    @app.errorhandler(401)
    def error(e):
        return render_template("401.html")
    
    return app
