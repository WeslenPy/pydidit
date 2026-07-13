
import hashlib
import hmac
import json


def shorten_floats(data):
    """Match Didit: whole-valued floats serialise as ints."""
    if isinstance(data, dict):
        return {k: shorten_floats(v) for k, v in data.items()}
    if isinstance(data, list):
        return [shorten_floats(x) for x in data]
    if isinstance(data, float) and data.is_integer():
        return int(data)
    return data



def hmac_verify(secret: str, payload: dict, signature: str) -> bool:
    
    canonical = json.dumps(
        shorten_floats(payload),
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    )
    expected = hmac.new(
        secret.encode("utf-8"),
        canonical.encode("utf-8"),
        hashlib.sha256
    ).hexdigest()

    if not hmac.compare_digest(signature, expected):
        return False
    
    
    return True