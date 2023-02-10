from dataclasses import dataclass


@dataclass
class User:
    name: str
    host: str
    port: str
    token: str
