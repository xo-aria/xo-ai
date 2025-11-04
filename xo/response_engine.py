from difflib import SequenceMatcher
from .find_matches import think_ai

def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

def clean_response(text):
    words = text.split()
    cleaned = []
    for w in words:
        if not cleaned or w != cleaned[-1]:
            cleaned.append(w)
    return " ".join(cleaned).strip()

def generate_response(msg, data, cache, memory):
    results = think_ai(msg, data)
    if not results:
        return "I'm not sure how to respond to that."

    cache.decay_scores()
    memory.decay()

    scored = []
    for r in results:
        category = r["category"]
        match = r["matched"]
        response = r["response"]

        present = match in msg.lower()
        position_weight = 1.5 if msg.lower().startswith(match) else 1.0
        cache.update_score(category, present, position_weight)

        base_sim = similarity(msg, match)
        cache_weight = cache.get_weight(category)
        total = (base_sim * 0.6) + (cache_weight * 0.4)
        scored.append((total, response, category))

        if present:
            memory.reinforce(category, match)

    best = max(scored, key=lambda x: x[0])
    memory.merge_with_database()
    return clean_response(best[1])
