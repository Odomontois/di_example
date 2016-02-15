import dialog


class User:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    prefix = property(doc="mariage status prefix")

    @prefix.getter
    def prefix(self):
        if hasattr(self, "_prefix"):
            return self._prefix
        if self.sex == "male":
            return "Mr"
        elif self.age < 22:
            return "Ms"
        else:
            return "Mrs"

    @prefix.setter
    def prefix(self, value):
        if value not in ("Mr", "Ms", "Mrs"):
            raise ValueError("enter Mr, Ms or Mrs")
        else:
            self._prefix = value

    @classmethod
    def by_dialog(cls):
        return cls(
            name=dialog.ask_name(),
            age=dialog.ask_age(),
            sex=dialog.ask_sex()
        )

    def __repr__(self):
        return "{prefix} {name} ({age})".format(
            prefix=self.prefix,
            **self.__dict__
        )
