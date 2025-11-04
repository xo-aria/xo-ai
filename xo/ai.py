import json
from .response_engine import generate_response

def load_database(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def main():
    db = load_database("data.json")
    print("XO is ready! Type your message (or 'exit' to quit)\n")
    while True:
        msg = input("You: ").strip()
        if msg.lower() in {"exit", "quit"}:
            break
        print("AI:", generate_response(msg, db))

if __name__ == "__main__":
    main()
