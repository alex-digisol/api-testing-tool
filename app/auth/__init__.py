import os
from flask import Blueprint

auth = Blueprint(
    "auth", 
    __name__, 
    url_prefix="/api/v1/auth"
)

GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", None)
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", None)
GOOGLE_DISCOVERY_URL = "https://accounts.google.com/.well-known/openid-configuration"


from . import views
from . import user