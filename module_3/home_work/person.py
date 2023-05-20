import datetime


class Person:

    def __init__(self, name: str, year_of_birth: int, address: str = ''):
        self.name = name
        self.yob = year_of_birth
        self.address = address

    def get_age(self) -> int:
        now = datetime.datetime.now()
        return now.year - self.yob

    def set_name(self, name: str) -> None:
        self.name = name

    def get_name(self) -> str:
        return self.name

    def set_address(self, address: str) -> None:
        self.address = address

    def get_address(self) -> str:
        return self.address

    def is_homeless(self) -> bool:
        """
        returns True if address is not set, false in other case
        """
        return self.address is None
