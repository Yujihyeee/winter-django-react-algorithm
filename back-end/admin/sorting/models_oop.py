from dataclasses import dataclass


@dataclass
class Calculator(object):
    num1 = int
    num2 = int

    @property
    def num1(self) -> int: return self._num1

    @property
    def num2(self) -> int: return self._num2

    @num2.setter
    def num2(self, num2): self._num2 = num2

    @num1.setter
    def num1(self, num1): self._num1 = num1

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiple(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2

class Grade(object):
    name = str
    kor = int
    eng = int
    math = int

    @property
    def name(self) -> str: return self._name
    @property
    def kor(self) -> int: return self._kor
    @property
    def eng(self) -> int: return self._eng
    @property
    def math(self) -> int: return self._math

    @name.setter
    def name(self, name): self._name = name
    @kor.setter
    def kor(self, kor): self._kor = kor
    @eng.setter
    def eng(self, eng): self._eng = eng
    @math.setter
    def math(self, math): self._math = math

    def sum(self):
        return self.kor + self.eng + self.math

    def average(self):
        return float(self.sum() / 3)

    def return_grade(self) -> str:
        aver = self.average()
        if aver >= 90:
            return 'A'
        elif aver >= 80:
            return 'B'
        elif aver >= 70:
            return 'C'
        elif aver >= 60:
            return 'D'
        elif aver >= 0:
            return 'F'


class Person(object):
    name = str
    age = int
    address = str


class Contacts(object):
    name = str
    phone = int
    email = str
    address = str

    @property
    def name(self) -> str: return self._name
    @name.setter
    def name(self, name): self._name = name

    @property
    def phone(self) -> int: return self._phone
    @phone.setter
    def phone(self, phone): self._phone = phone

    @property
    def email(self) -> str: return self._email
    @email.setter
    def email(self, email): self._email = email

    @property
    def address(self) -> str: return self._address
    @address.setter
    def address(self, address): self._address = address

    def to_string(self):
        print(f'name is {self.name}, phone is {self.phone}, email is {self.email}, address is {self.address}.')

    @staticmethod
    def set_contact(name, phone, email, address) -> object:
        return Contacts(name, phone, email, address)

    @staticmethod
    def get_contacts(ls):
        for i in ls:
            i.to_string()
        return ls

    @staticmethod
    def del_contact(ls, name):
        for i, v in enumerate(ls):
            if name == v.name:
                del ls[i]
        return ls