import sys
from .ai_core import AI

def show_help():
    print("""
XO AI Commands:
  run       → Start interactive chat
  train     → Merge learned memory into database
  reset     → Clear short-term memory (cache)
  help      → Show this help message
    """)

def run_cli():
    args = sys.argv[1:]
    if not args:
        return show_help()

    cmd = args[0].lower()
    bot = AI("data.json")

    if cmd == "run":
        print("XO is ready! Type 'exit' to quit.\n")
        while True:
            msg = input("You: ").strip()
            if msg.lower() in {"exit", "quit"}:
                break
            print("AI:", bot.ask(msg))

    elif cmd == "train":
        bot.retrain()
        print("[+] Model retrained and memory merged into data.json")

    elif cmd == "reset":
        bot.reset_memory()
        print("[+] Cache cleared successfully.")

    elif cmd == "help":
        show_help()
    else:
        print(f"[-] Unknown command: {cmd}")
        show_help()
