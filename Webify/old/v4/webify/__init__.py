from typing import Iterable, Callable


class WebApp:
    def __init_subclass__(cls, api_path: Iterable[str] = ('api',), html_path: Iterable[str] = (), **kwargs: Any) -> None:
        cls.routes = RecursiveDefaultDict()
        
        for name, value in vars(cls).items():
            if not value.startswith('_'):
                if isinstance(value, type):
                    cls.routes[name].update(htmlify_class(value))
                    cls.routes[api_path][name].update(apify_class(value))
                elif isinstance(value, Callable):
                    cls.routes[name][''] = htmlify_callable(value)
                    cls.routes[api_path][name][''] = apify_callable(value)
                else:
                    cls.routes[name][''] = htmlify_callable(constant(value))
                    cls.routes[api_path][name][''] = apify_callable(constant(value))
