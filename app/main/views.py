from flask import render_template
from app.typedefs import Project, generate_static_projects
from typing import List
from . import main
from flask_login import login_required


@main.route("/")
@login_required
def home():
    return render_template("home/index.html", projects=generate_static_projects(5)), 200