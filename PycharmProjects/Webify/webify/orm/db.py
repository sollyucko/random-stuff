class Row:
    def __init__(self, **values):
        pass

    def __init_subclass__(cls, table_name: str = None, db: DBIdentifier = None):
        cls._table_name_ = cls.__name__ if table_name is None else table_name
