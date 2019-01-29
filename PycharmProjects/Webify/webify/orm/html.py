from html import escape

import regex  # type: ignore


split_camel_case = regex.compile(  # pylint: disable=invalid-name
    r"(?<=[[:lower:]])(?=[[:upper:]])"
).split


def html(obj: object) -> str:
    try:
        return str(type(obj).__html__(obj))  # type: ignore
    except (AttributeError, TypeError):
        try:
            return obj.__html__()  # type: ignore
        except (AttributeError, TypeError):
            try:
                return obj.__html__(obj)  # type: ignore
            except (AttributeError, TypeError):
                return str(obj)


class Element:
    def __init__(self, *args, **kwargs):
        """
        **kwargs is for attributes in base class and values in subclasses.
        Subclass __init__ is mainly designed for forms.
        """

        if type(self) is Element:  # pylint: disable=unidiomatic-typecheck
            self.tag_name, *self.children = args
            self.attributes.update(kwargs)
        else:
            for name, value in kwargs.items():
                if name.endswith("_"):  # Allow passing self as a value.
                    name = name[:-1]

                setattr(self, name, getattr(self, name)(value=value))

    def __init_subclass__(cls, **attributes):
        cls.attributes = attributes
        cls.children = [
            value for name, value in vars(cls).items() if not name.startswith("_")
        ]
        cls.tag_name = split_camel_case(cls.__name__)[-1].lower()

    def __html__(self):
        """Works on instances and subclasses."""
        formatted_attributes = "".join(
            f' {name}="{escape(str(value))}"' for name, value in self.attributes.items()
        )

        if self.children:
            return f"<{self.tag_name}{formatted_attributes}>{''.join(map(html, self.children))}</{self.tag_name}>"

        return f"<{self.tag_name}{formatted_attributes} />"

    def __repr__(self):
        return f"Element({})"
