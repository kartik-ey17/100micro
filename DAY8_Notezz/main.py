from dataclasses import dataclass

@dataclass
class Note:
    id: int
    title: str
    content: str

class NotesApp:
    def __init__(self):
        self.notes: list[Note] = []
        self.nextId: int = 1

    def create_note(self):
        print("----- Create Note -----")
        title = input("Title: ").strip()
        if not title:
            print("Title cannot me empty.")
            return
        print("Content : ")
        content = input("> ").strip()

        note = Note(id=self.nextId , title=title , content=content)
        self.notes.append(note)
        self.nextId += 1

    def view_notes(self):
        print("----- Your Notes -----")
        if not self.notes:
            print("No notes available.")
            return
        for note in self.notes:
            print(f"{note.id}.  {note.title}")

        choice = input("Enter note ID to read full content : ").strip()
        if choice.isdigit():
            target_id = int(choice)
            self.read_note(target_id)

    def read_note(self , note_id):
        for note in self.notes:
            if note.id == note.id:
                print("------------------------")
                print(f"{note.id}.  {note.title} : ")
                print(note.content)
                print("------------------------")
                return
        print(f"Note with ID {note_id} not found.")

    def search_notes(self):
        print("----- Search Notes -----")
        query = input("Enter search keyword: ").strip().lower()
        if not query:
            print("Search query cannot be empty.")
            return

        results = [n for n in self.notes if query in n.title.lower() or query in n.content.lower()]

        if not results:
            print(f"No notes found matching {query}")
            return

        print(f"\nFound {len(results)} matching notes.")

        for note in results:
            print(f"{note.id}.  {note.title}")

    def delete_note(self):
        print("----- Delete Note -----")
        try:
            target_id = int(input("Enter Note ID to delete : "))
        except ValueError:
            print("Invalid ID format.")
            return

        for i , note in enumerate(self.notes):
            if note.id == target_id:
                deleted = self.notes.pop(i)
                print(f"Deleted note ID {target_id} ({deleted.title}).")
                return

        print(f"No note found with ID {target_id}")

    def run(self):
        while True:
            print("+=+=+= Notes =+=+=+")
            print("1. Create notes\n2. View notes\n3. Search notes\n4. Delete notes\n5. Exit")

            choice = int(input("\nChoose an option (1-5)"))

            if choice == 1:
                self.create_note()
            elif choice == 2:
                self.view_notes()
            elif choice == 3:
                self.search_notes()
            elif choice == 4:
                self.delete_note()
            elif choice == 5:
                print("Sayonara ~ ~")
                break
            else:
                print("Invalid option.")

app = NotesApp()
app.run()