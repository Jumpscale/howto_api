import requests


from .Group import Group
from .User import User

from .client import Client as APIClient


class Client:
    def __init__(self, base_uri="http://127.0.0.1:5000/"):
        self.api = APIClient(base_uri)
        