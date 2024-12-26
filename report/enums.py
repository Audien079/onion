from admin.enum import BaseStrEnum


class WebType(BaseStrEnum):
    """
    Website type enum
    """

    PROXY = "PROXY"
    SEARCH = "SEARCH"
    CONTENT = "CONTENT"
