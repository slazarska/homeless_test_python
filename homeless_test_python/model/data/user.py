from dataclasses import dataclass


@dataclass
class User:
    name: str
    email: str


test_user = User(
    name='Святослав Вернидубович Кривич',
    email='krivich@smolensk.org')
