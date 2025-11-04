import json
from .cache_system import TopicCache
from .memory_system import AILongMemory
from .response_engine import generate_response
from .database import load_database

class AI:
    def __init__(self, db_path="data.json"):
        self.db_path = db_path
        self.data = load_database(db_path)
        self.cache = TopicCache()
        self.memory = AILongMemory(db_path)

    def ask(self, message: str):
        return generate_response(message, self.data, self.cache, self.memory)

    def retrain(self):
        self.memory.merge_with_database()
        self.data = load_database(self.db_path)

    def reset_memory(self):
        self.cache.scores.clear()
        self.cache.save_cache()

    def stats(self):
        return {
            "cache": dict(self.cache.scores),
            "memory": self.memory.memory
        }
