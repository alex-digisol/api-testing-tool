import random
from uuid import uuid4, UUID
from typing import Union
from datetime import datetime
from dataclasses import dataclass, asdict
from app.utils import random_string
from enum import Enum


class Methods(Enum):
    GET = "GET"
    POST = "POST"
    PATCH = "PATCH"
    PUT = "PUT"
    DELETE = "DELETE"


@dataclass
class Project:
    id: UUID
    name: str
    description: str
    # TODO: owner
    created_at: datetime


@dataclass
class Endpoint:
    id: UUID
    project_id: UUID
    method: Methods
    url: str
    name: str
    description: str
    created_at: datetime
    # TODO: saved response


def generate_static_projects(length: int):
    for i in range(0, length):
        yield asdict(Project(id=uuid4(), name=random_string(10), description=random_string(10), created_at=datetime.now()))


def generate_endpoints(id: UUID, length: int) -> Endpoint:
    for i in range(0, length):
        yield asdict(generate_endpoint(id))


def generate_endpoint(id: UUID) -> Endpoint:
    return Endpoint(
        id=id,
        project_id=uuid4(),
        method=random.choice(list(Methods)),
        name=random_string(10),
        url=f"http://localhost:8000/api/v2/test/{random_string(10)}",
        description=random_string(10),
        created_at=datetime.now(),
    )
