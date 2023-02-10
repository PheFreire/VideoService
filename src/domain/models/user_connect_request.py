from dataclasses import dataclass


@dataclass
class UserConnectRequest:
    name: str
    password: str
    keep_connect: bool
