try:
    from starlette_marshal import rapidjson as json
except ImportError:
    import json

try:
    from starlette_marshal.rapidjson import RapidJSONResponse as JSONResponse
except ImportError:
    from starlette.responses import JSONResponse
