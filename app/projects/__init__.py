from flask import Blueprint

projects = Blueprint("projects", __name__)

from . import projects
from . import views