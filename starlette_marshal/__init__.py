try:
    from starlette_marshal import rapidjson as json
except ImportError:
    import json  # noqa: F401

try:
    from starlette_marshal.rapidjson import RapidJSONResponse as JSONResponse
except ImportError:
    from starlette.responses import JSONResponse  # noqa: F401

__version__ = "0.1.0"
