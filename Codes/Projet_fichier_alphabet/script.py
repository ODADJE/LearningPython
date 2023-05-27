from pathlib import Path

file = Path(__file__).parent / "text.txt"

with open(file, "r") as f:
    texts = f.read().splitlines()
    firstnames = []
    for text in texts:
        firstnames.extend(text.split())
    firstnames = [firstname.strip(",. ") for firstname in firstnames] 
    firstnames.sort()

final_file = Path(__file__).parent / "final.txt"
if final_file.exists():
    final_file.unlink()
final_file.touch()

with open(final_file, "a") as f:
    #for name in text:
    f.write("\n".join(firstnames))

