import time
import json
from collections import defaultdict

CACHE_FILE = ".cache.xo"
DECAY_RATE = 0.9
DECAY_INTERVAL = 60

class TopicCache:
    def __init__(self):
        self.scores = defaultdict(float)
        self.last_update = time.time()
        self.load_cache()

    def load_cache(self):
        try:
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.scores = defaultdict(float, data.get("scores", {}))
                self.last_update = data.get("last_update", time.time())
        except FileNotFoundError:
            pass

    def save_cache(self):
        with open(CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump({"scores": self.scores, "last_update": self.last_update}, f, ensure_ascii=False, indent=2)

    def decay_scores(self):
        now = time.time()
        if now - self.last_update >= DECAY_INTERVAL:
            for k in list(self.scores.keys()):
                self.scores[k] *= DECAY_RATE
            self.last_update = now
            self.save_cache()

    def update_score(self, category: str, present: bool, position_weight: float = 1.0):
        base = 1.0 if present else -0.5
        self.scores[category] += base * position_weight
        self.save_cache()

    def get_weight(self, category: str) -> float:
        return self.scores.get(category, 0.0)
