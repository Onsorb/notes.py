from pathlib import Path

FILE_NAME = "notes.txt"

def get_notes_from_user():
    print("یادداشت‌ها را وارد کنید. برای پایان، یک خط خالی بزنید:")
    notes = []
    while True:
        line = input("> ").strip()
        if line == "":
            break
        notes.append(line)
    return notes

def save_notes(notes, filename=FILE_NAME):
    if not notes:
        return
    with open(filename, "a", encoding="utf-8") as f:
        for n in notes:
            f.write(n + "\n")

def read_notes(filename=FILE_NAME):
    path = Path(filename)
    if not path.exists():
        return []
    with open(filename, "r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f if line.strip() != ""]

def print_numbered(notes):
    if not notes:
        print("یادداشتی وجود ندارد.")
        return
    print("\nیادداشت‌ها:")
    for i, n in enumerate(notes, start=1):
        print(f"{i}. {n}")

def main():
    notes = get_notes_from_user()
    save_notes(notes)
    all_notes = read_notes()
    print_numbered(all_notes)

if __name__ == "__main__":
    main()
