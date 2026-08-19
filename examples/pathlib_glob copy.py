## Example

from pathlib import Path

for file in Path('.').glob('*.py'):
    print(file)

