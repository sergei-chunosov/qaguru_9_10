from dataclasses import dataclass


@dataclass
class User:
    name: str
    lastname: str
    email: str
    gender: str
    phone: str
    birthday: list
    subjects: str
    hobby: str
    picture: str
    address: str
    state: str
    city: str
