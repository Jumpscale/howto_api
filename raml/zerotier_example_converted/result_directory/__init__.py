import requests


from .ControllerMemberConfig import ControllerMemberConfig
from .ControllerNetworkConfig import ControllerNetworkConfig
from .GlobalPermissions import GlobalPermissions
from .Member import Member
from .Network import Network
from .Permissions import Permissions
from .RandomToken import RandomToken
from .Status import Status
from .User import User
from .id import id

from .client import Client as APIClient


class Client:
    def __init__(self, base_uri="https://my.zerotier.com/"):
        self.api = APIClient(base_uri)
        