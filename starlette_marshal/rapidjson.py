from json import JSONDecoder, JSONEncoder
from typing import Type, Callable, Any, Union

from rapidjson import (  # noqa: F401
    dump,
    dumps as rapidjson_dumps,
    load,
    loads as rapidjson_loads,
    Decoder,
    JSONDecodeError,
    RawJSON,
    ValidationError,
    Validator,
    BM_NONE,
    BM_UTF8,
    DM_IGNORE_TZ,
    DM_ISO8601,
    DM_NAIVE_IS_UTC,
    DM_NONE,
    DM_ONLY_SECONDS,
    DM_SHIFT_TO_UTC,
    DM_UNIX_TIME,
    IM_ANY_ITERABLE,
    IM_ONLY_LISTS,
    MM_ANY_MAPPING,
    MM_COERCE_KEYS_TO_STRINGS,
    MM_ONLY_DICTS,
    MM_SKIP_NON_STRING_KEYS,
    MM_SORT_KEYS,
    NM_DECIMAL,
    NM_NAN,
    NM_NATIVE,
    NM_NONE,
    PM_COMMENTS,
    PM_NONE,
    PM_TRAILING_COMMAS,
    UM_CANONICAL,
    UM_HEX,
    UM_NONE,
    WM_COMPACT,
    WM_PRETTY,
    WM_SINGLE_LINE_ARRAY,
)
from starlette.responses import Response


def dumps(
    obj: Any,
    *,
    skipkeys: bool = False,
    ensure_ascii: bool = True,
    check_circular: bool = True,  # noqa
    allow_nan: bool = True,
    cls: Type[JSONEncoder] = None,  # noqa
    indent: Union[None, int, str] = None,
    separators: tuple[str, str] = None,  # noqa
    default: Callable = None,
    sort_keys: bool = False,
    **kwargs: Any,
) -> str:
    return rapidjson_dumps(
        obj=obj,
        skipkeys=skipkeys,
        ensure_ascii=ensure_ascii,
        allow_nan=allow_nan,
        indent=indent,
        default=default,
        sort_keys=sort_keys,
        **kwargs,
    )


def loads(
    s: Union[str, bytes],
    *,
    cls: Type[JSONDecoder] = None,  # noqa
    object_hook: Callable[[dict], Any] = None,
    parse_float: Callable[[str], Any] = None,  # noqa
    parse_int: Callable[[str], Any] = None,  # noqa
    parse_constant: Callable[[str], Any] = None,  # noqa
    object_pairs_hook: Callable[[list[tuple[Any, Any]]], Any] = None,  # noqa
    **kwargs: Any,
) -> Any:
    return rapidjson_loads(
        string=s,
        object_hook=object_hook,
        **kwargs,
    )


class RapidJSONResponse(Response):
    media_type = "application/json"

    def render(self, content: Any) -> bytes:
        return dumps(
            content,
            ensure_ascii=False,
            allow_nan=False,
            indent=None,
            uuid_mode=UM_CANONICAL,
            datetime_mode=DM_ISO8601,
        ).encode("utf-8")
