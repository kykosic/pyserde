import json

SMALL = '{"i": 10, "s": "foo", "f": 100.0, "b": true}'

SMALL_TUPLE = (10, "foo", 100.0, True)

SMALL_DICT = json.loads(SMALL)

MEDIUM = f'{{"inner": [{",".join([SMALL] * 50)}]}}'

MEDIUM_TUPLE = tuple([[SMALL_TUPLE] * 50])

json_md = (
    '{"i": 10, "s": "foo", "f": 100.0, "b": true,'
    '"i2": 10, "s2": "foo", "f2": 100.0, "b2": true,'
    '"i3": 10, "s3": "foo", "f3": 100.0, "b3": true,'
    '"i4": 10, "s4": "foo", "f4": 100.0, "b4": true,'
    '"i5": 10, "s5": "foo", "f5": 100.0, "b5": true}'
)

json_pri_container = (
    '{"v": [1, 2, 3, 4, 5], "d": {"foo": 10, "fuga": 20}, "foo": 30, "t": [true, false, true]}'
)

args_sm = {"i": 10, "s": "foo", "f": 100.0, "b": True}

args_md = [args_sm] * 50
