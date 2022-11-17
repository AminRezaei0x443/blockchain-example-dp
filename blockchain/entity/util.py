import json
from hashlib import sha256


def dict_hash(d: dict):
    data_s = json.dumps(d)
    return sha256(data_s.encode("utf-8")).hexdigest()
