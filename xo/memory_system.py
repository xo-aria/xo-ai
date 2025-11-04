import json
import os
from collections import defaultdict

MEMORY_FILE = ".memory.xo"

class AILongMemory:
    def __init__(self, data_path="data.json"):
        self.data_path = data_path
        self.memory = defaultdict(lambda: defaultdict(int))
        self.load_memory()

    def load_memory(self):
        if os.path.exists(MEMORY_FILE):
            try:
                with open(MEMORY_FILE, "r", encoding="utf-8") as f:
                    self.memory = json.load(f)
            except Exception:
                self.memory = defaultdict(lambda: defaultdict(int))

    def save_memory(self):
        with open(MEMORY_FILE, "w", encoding="utf-8") as f:
            json.dump(self.memory, f, ensure_ascii=False, indent=2)

    def reinforce(self, category: str, phrase: str):
        if category not in self.memory:
            self.memory[category] = {}
        self.memory[category][phrase] = self.memory[category].get(phrase, 0) + 1
        self.save_memory()

    def decay(self, rate=0.95):
        for category in list(self.memory.keys()):
            for phrase in list(self.memory[category].keys()):
                self.memory[category][phrase] *= rate
        self.save_memory()

    def merge_with_database(self):
        if not os.path.exists(self.data_path):
            return
        with open(self.data_path, "r", encoding="utf-8") as f:
            db = json.load(f)

        for category, phrases in self.memory.items():
            if category not in db:
                db[category] = {}
            for phrase, score in phrases.items():
                if score >= 3 and phrase not in db[category]:
                    db[category][phrase] = f"I've learned this phrase: {phrase}"

        with open(self.data_path, "w", encoding="utf-8") as f:
            json.dump(db, f, ensure_ascii=False, indent=2)
