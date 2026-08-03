from pathlib import Path

MAX_ATTEMPTS = 6
WORDS_FILE = Path(__file__).parent / "words.txt"

p = Path('llm/claude/main.py')
print(p.name)
print(p.stem)
print(p.suffix)
print(p.parts)
print(p.parent)
