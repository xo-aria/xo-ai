import os
import json
import pickle
import hashlib
from difflib import get_close_matches
from typing import Any, Dict, List

MODEL_DIR = ".ai_models"

def _make_hash_for_db(data: Dict[str, Dict[str, str]]) -> str:
    j = json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(j.encode("utf-8")).hexdigest()

def _model_path_for_hash(h: str) -> str:
    os.makedirs(MODEL_DIR, exist_ok=True)
    return os.path.join(MODEL_DIR, f"lookup_{h}.pkl")

def _build_lookup(data: Dict[str, Dict[str, str]]) -> Dict[str, tuple]:
    lookup: Dict[str, tuple] = {}
    for category, phrases in data.items():
        for phrase, reply in phrases.items():
            lookup[phrase] = (category, reply)
    return lookup

def _save_model(path: str, lookup: Dict[str, tuple]) -> None:
    with open(path, "wb") as f:
        pickle.dump(lookup, f)

def _load_model(path: str) -> Dict[str, tuple]:
    with open(path, "rb") as f:
        return pickle.load(f)

def get_lookup_cached(data: Dict[str, Dict[str, str]], force_rebuild: bool = False) -> Dict[str, tuple]:
    h = _make_hash_for_db(data)
    path = _model_path_for_hash(h)

    if not force_rebuild and os.path.exists(path):
        try:
            lookup = _load_model(path)
            return lookup
        except Exception:
            pass

    lookup = _build_lookup(data)
    try:
        _save_model(path, lookup)
    except Exception:
        pass
    return lookup

def think_ai(msg: str, data: Dict[str, Dict[str, str]], force_rebuild: bool = False) -> List[Dict[str, str]]:
    mesg = msg.lower().strip()
    lookup = get_lookup_cached(data, force_rebuild=force_rebuild)

    words = mesg.split()

    found = []
    for word in words:
        matches = get_close_matches(word, lookup.keys(), n=1, cutoff=0.5)
        if matches:
            phrase = matches[0]
            cat, res = lookup[phrase]
            found.append({'word': word, 'matched': phrase, 'category': cat, 'response': res})

    if not found:
        return [{'category': 'unknown', 'response': "sorry, i didn't understand that."}]
    return found
