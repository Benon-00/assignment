 Example

from pathlib import Path

new_dir = Path("example.txt")
new_dir.write_text('hello')
print(new_dir.is_file())

