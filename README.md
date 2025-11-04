[![Downloads](https://pepy.tech/badge/xo-ai)](https://pepy.tech/project/xo-ai)
[![PyPI version](https://img.shields.io/pypi/v/xo-ai.svg)](https://pypi.org/project/xo-ai/)
![Django](https://img.shields.io/badge/Django-3.2%20|%204.2%20|%205.0-green?logo=django)
[![License](https://img.shields.io/github/license/xo-aria/xo-ai)](https://github.com/xo-aria/xo-ai/blob/main/LICENSE)
![Status](https://img.shields.io/badge/status-active-brightgreen)

![XO](xo.jpg)
# XO AI 🤖

**XO — Minimal Conversational Intelligence Framework with Memory & Reinforcement Learning**

XO is a lightweight, modular conversational AI framework designed for developers who want to build intelligent, context-aware, and self-improving chat systems.
It combines short-term caching, long-term memory, and reinforcement-style learning to create natural, adaptive responses.

---

## 🚀 Features

* **Reinforcement Learning** — XO learns from repeated user interactions.
* **Short-Term Cache System** — Prioritizes frequently used topics dynamically.
* **Long-Term Memory** — Persists knowledge across sessions.
* **CLI & SDK Modes** — Use XO from code or command line.
* **Modular & Editable** — Every logic layer (cache, memory, response) can be customized.
* **Lightweight & Fast** — Zero external heavy dependencies.

---

## 🔧 Installation

### From PyPI

```bash
pip install xo-ai
```

### From Source

```bash
git clone https://github.com/xo-aria/xo-ai.git
cd xo-ai
pip install .
```

---

## 💻 Usage

### 🔹 As a Python Library (SDK)

```python
from xo import AI

bot = AI("data.json")
response = bot.ask("hi")
print(response)
```

### 🔹 As Command Line Tool

XO provides a built-in CLI for easy interaction:

```python
from xo.cli import run_cli

if __name__ == "__main__":
    run_cli()
```
And use cli in cmd:
```bash
xo run     # Start an interactive chat
xo train   # Merge long-term memory into database
xo reset   # Clear short-term cache
xo help    # Show command help
```

---

## 🧠 How XO Learns

* Each repeated phrase increases its weight in memory (reinforcement).
* Topics decay over time if unused.
* When repetition threshold is reached, new learned patterns are merged into `data.json` automatically.

---

## 🖊️ Example Data File

```json
{
  "conversation": {
    "hi": "hello there!",
    "how are you": "Howdy! What can I do for you?"
  },
  "shop": {
    "price": "The price varies by product. Which item interests you?"
  }
}
```

---

## 👩‍💻 For Developers

XO was built to be easily modifiable:

* **cache_system.py** → short-term memory logic.
* **memory_system.py** → reinforcement & decay logic.
* **response_engine.py** → natural response selection.
* **cli.py** → command-line interface.

You can modify these independently without breaking the framework.

---

## 🎨 Example CLI Output

```bash
$ xo run
XO is ready! Type 'exit' to quit.

You: hi
AI: hello there!

You: how are you
AI: Howdy! What can I do for you?
```

---

## 🔗 Links

* **Homepage:** [https://github.com/xo-aria/xo-ai](https://github.com/xo-aria/xo-ai)
* **Repository:** [https://github.com/xo-aria/xo-ai](https://github.com/xo-aria/xo-ai)
* **Issues:** [https://github.com/xo-aria/xo-ai/issues](https://github.com/xo-aria/xo-ai/issues)
* **License:** MIT

---

## 💎 Credits

Created with ❤️ by **XO Aria**
Designed for developers who believe AI should be both *smart* and *simple*.
