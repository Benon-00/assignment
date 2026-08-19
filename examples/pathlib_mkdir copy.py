 Example

from pathlib import Path

new_dir = Path("output/reports")
new_dir.mkdir(parents=True, exist_ok=True)
print(new_dir.exists())

