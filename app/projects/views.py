from uuid import UUID
from app.typedefs import generate_endpoints, Endpoint
from typing import List
from flask import render_template
from flask_login import login_required
from . import projects


@projects.route("/projects/<project_id>", methods=["GET"])
@login_required
def project_detail(project_id):
    # project = Project(id=project_id)
    project = {"id": UUID(project_id)}
    endpoints: List[Endpoint] = generate_endpoints(id=project["id"], length=10)
    return render_template(
        "projects/detail.html",
        project=project, 
        endpoints=endpoints
    ), 200



@projects.route("/projects/<project_id>/endpoint/<endpoint_id>", methods=["GET"])
@login_required
def endpoint_detail(project_id, endpoint_id):
    # project = Project(id=project_id)
    project = {"id": UUID(project_id)}
    endpoints: List[Endpoint] = generate_endpoints(id=project["id"], length=10)
    return render_template(
        "projects/endpoint-detail.html",
        project=project, 
        endpoints=endpoints
    ), 200


@projects.route("/projects/create", methods=["GET"])
@login_required
def project_create():
    return render_template("projects/create.html"), 200