from enum import Enum, IntEnum


class BaseStrEnum(Enum):
    """Base Str Enum"""

    def __str__(self):
        return f"{self.value}"

    @classmethod
    def has_name(cls, name):
        """
        chek if name exists
        """
        return any(str(name) == str(item.name) for item in cls)

    @classmethod
    def has_value(cls, value):
        """
        check if value exists
        """
        return any(str(value) == str(item.value) for item in cls)

    @classmethod
    def choices(cls):
        """
        choices tuple list
        """
        return [(key.name, key.value) for key in cls]


class BaseIntEnum(IntEnum):
    """
    Base Int Enum
    """

    @classmethod
    def choices(cls):
        """
        Choices
        """
        return [(key.name, key.value) for key in cls]

    @classmethod
    def display_choices(cls):
        """
        Display choices
        """
        return [(key.value, key.value) for key in cls]
