from dataclasses import dataclass


@dataclass
class UserRegister:
    name: str
    password: str
    email: str
    keep_connect: bool
