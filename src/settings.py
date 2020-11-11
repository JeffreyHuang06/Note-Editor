import json
from src.args import _args
_settings = dict()

with open(_args.json, "r") as jsn:
    _settings = json.load(jsn)