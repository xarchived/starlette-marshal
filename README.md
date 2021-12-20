# Starlette Marshal

This package has two usage.Provide a "JSONResponse" to replace simple Starlette
"JSONResponse" and works with other Python JSON libraries. And offer a "json"
library to replace Python "json" library, so we can use it instead.

## Installation

To install base package:

```bash
pip install -U starlette-marshal
```

to support RapidJSON:

```bash
pip install -U starlette-marshal[rapidjson]
```

or if you prefer the latest development version, you can install it from the source:

## Quickstart

We want to be soft dependency. So this package is 100% compatible with standard Python and Starlette package. To archive
this goal you can import it like this:

```python
try:
    from starlette_marshal import json
except ImportError:
    import json

try:
    from starlette_marshal import JSONResponse
except ImportError:
    from starlette.responses import JSONResponse

```

the usage is just like Starlette itself:

```python
async def get(request: Request) -> Response:
    content: dict = {
        'foo': 'This is foo',
        'bar': 'And here the bar',
    }
    return JSONResponse(content=content)
```

and for "json" library:

```python
async def post(request: Request) -> Response:
    body: dict = json.loads(s=await request.body())
    return JSONResponse(content=body)
```

## TODO

- [x] Support RapidJSON
- [ ] Support UltraJSON
- [ ] Support simplejson
- [ ] Support orjson
