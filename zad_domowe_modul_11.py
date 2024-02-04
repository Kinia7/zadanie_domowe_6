from datetime import datetime

class Field:
    def __init__(self, value=None):
        self._value = value

    def __str__(self):
        return str(self._value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

class Phone(Field):
    def __init__(self, value=None):
        super().__init__(value)
        self.validate()

    def validate(self):
        pass

class Birthday(Field):
    def __init__(self, value=None):
        super().__init__(value)
        self.validate()

    def validate(self):
        pass

class Record:
    def __init__(self, name, phone, email, birthday=None):
        self.name = Field(name)
        self.phone = Phone(phone)
        self.email = Field(email)
        self.birthday = Birthday(birthday)

    def days_to_birthday(self):
        if self.birthday.value:
            today = datetime.today()
            next_birthday = datetime(today.year, self.birthday.value.month, self.birthday.value.day)
            if today > next_birthday:
                next_birthday = datetime(today.year + 1, self.birthday.value.month, self.birthday.value.day)
            delta = next_birthday - today
            return delta.days
        else:
            return None

class AddressBook:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < len(self.records):
            result = self.records[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration
