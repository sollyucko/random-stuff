from __future__ import annotations

from typing import Iterable, Type


# class MergedObjectMeta(type):
#     def __getattribute__(cls, name):
#         if cls is MergedObject:
#             return super().__getattribute__(name)

#         merged_objects = object.__getattribute__(cls, "_merged_objects")

#         if name in {"__getattribute__", "__getattr__"}:
#             return object.__getattribute__(cls, name)
#         else:
#             for obj in merged_objects:
#                 try:
#                     return getattr(obj, name)
#                 except AttributeError:
#                     pass

#     def __dir__(cls):
#         result = set()

#         for obj in object.__getattribute__(cls, "_merged_objects"):
#             result.update(dir(type(obj)))

#         return result

#     @property
#     def __dict__(cls):
#         result = {}

#         for obj in object.__getattribute__(cls, "_merged_objects"):
#             result.update(vars(type(obj)))

#         print(result)
#         return result


# class MergedObject(metaclass=MergedObjectMeta):
#     def __new__(cls, merged_objects):
#         return MergedObjectMeta(''.join(type(obj).__name__ for obj in merged_objects), (cls,), {'_merged_objects': merged_objects})(merged_objects)

#     def __dir__(self):
#         result = set()

#         for obj in object.__getattribute__(self, "_merged_objects"):
#             result.update(dir(obj))

#         return result

#     def __getattribute__(self, attribute):
#         for obj in object.__getattribute__(self, "_merged_objects"):
#             try:
#                 return getattr(obj, attribute)
#             except AttributeError as ex:
#                 pass

#         raise AttributeError("Attribute not found on any subobject")


def singleton_class(obj: object) -> Type[object]:
    class Class(type(obj)):  # type: ignore
        def __init__(self):
            pass

        def __getattribute__(self, name):
            try:
                return getattr(obj, name)
            except AttributeError:
                return super().__getattribute__(name)

    Class.__name__ = Class.__qualname__ = f"singleton_class({obj!r})"
    Class.__module__ = singleton_class.__module__
    return Class


def merge_objects(*objects: Iterable[object]) -> object:
    def __dir__(self):
        result = set()

        for obj in objects:
            result.update(dir(obj))

        return result

    def __getattribute__(self, name):
        if name == "__dict__":
            result = {}

            for obj in reversed(objects):  # Earlier ones should override later ones.
                result.update(vars(obj))

            result.update(namespace)
            return result
        elif name == "__class__":
            return cls
        else:
            return super(cls, self).__getattribute__(name)

    namespace = {"__dir__": __dir__, "__getattribute__": __getattribute__}

    cls = type(
        f"merge_objects({', '.join(map(repr, objects))})",
        tuple(map(singleton_class, objects)),
        namespace,
    )
    cls.__module__ = merge_objects.__module__
    return cls()
