import time
from datetime import datetime
import json
from pathlib import Path
from dataclasses import dataclass , asdict

@dataclass
class DiaryEntry:
    id: int
    title: str
    content: str
    mood: str
    created_at: str
    updated_at: str

class DearDiary:
    def __init__(self , filename: str = "diary.json"):
        self.filepath = Path(filename)
        self.entries: list[DiaryEntry] = []
        self.nextId: int = 1
        self.load()

    def load(self):
        if not self.filepath.exists():
            return
        try:
            with open(self.filepath, "r" , encoding="utf-8") as f:
                data = json.load(f)
                self.entries = [DiaryEntry(**item) for item in data]
                if self.entries:
                    self.nextId = max(entry.id for entry in self.entries) + 1
        except (json.JSONDecodeError , TypeError) as e:
            print(f"Could not read {self.filepath} ({e}).")

    def save(self):
        with open(self.filepath , "w" , encoding="utf-8") as f:
            json.dump([asdict(entry) for entry in self.entries], f , indent = 4)

    def create_entry(self):
        print("\n+=+=+= New Diary Entry =+=+=+")
        time.sleep(2)
        title = input("Give today a title ! : ").strip()
        if not title:
            print("A title should not be empty I guess?")
            return

        print("\nChoose an emoji to describe your day today among(😃/😟/✨/😐/💔/😭)")
        mood = input("Choose : ").strip() or "❤️"

        print("\nWrite your day :")
        content = input("> ").strip()
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        entry = DiaryEntry(
            id=self.nextId,
            title=title,
            content=content,
            mood=mood,
            created_at= now,
            updated_at= now,
        )
        self.entries.append(entry)
        self.nextId += 1
        self.save()
        print("Saved your day in the diary :)")
        time.sleep(3)

    def view(self , entry_list: list[DiaryEntry] | None=None):
        print("\n+=+=+= My Diary =+=+=+")
        target_list = self.entries if entry_list is None else entry_list

        if not target_list:
            print("No entries found.")
            return

        for e in target_list:
            print(f"{e.id}.   {e.created_at}   {e.mood}   {e.title}")
        print("*"*20)
        time.sleep(2)
        choice = input("Enter diary ID to read(press enter for none) : ").strip()
        if choice.isdigit():
            self.read_entry(int(choice))

    def read_entry(self , entry_id):
        for e in self.entries:
            if e.id == entry_id:
                print(f"{e.id}. | {e.mood} | {e.created_at}  ")
                if e.created_at != e.updated_at:
                    print(f"(Last edited: {e.updated_at})")
                print(f"{e.title}.")
                print("*"*20)
                print(e.content)
                print("_"*30)
                time.sleep(7)
                return
        print(f"There is no written Diary with ID {entry_id}.")

    def update(self):
        print("\n+=+=+= Edit your Diary =+=+=+")
        try:
            target_id = int(input("Enter Diary ID to edit: "))
        except ValueError:
            print("Invalid ID format.")
            return

        for e in self.entries:
            if e.id == target_id:
                print(f"\nEditing Entry #{e.id}.  {e.title}")
                new_title = input(f"New title [{e.title}]: ").strip()
                new_mood = input(f"New mood [{e.mood}]: ").strip()
                print(f"Current content: {e.content}")
                time.sleep(3)
                new_content = input("New content (blank to keep unchanged) : ").strip()
                if new_title:
                    e.title = new_title
                if new_mood:
                    e.mood = new_mood
                if new_content:
                    e.content = new_content

                e.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save()
                print("Diary updated :)")
                time.sleep(2)
                return
        print("No diary found with that id :( ")

    def delete_entry(self):
        print("\n+=+=+= Delete Diary =+=+=+")
        try:
            target_id = int(input("Enter diary ID to delete: "))
        except ValueError:
            print("Invalid ID format.")
            return
        for i,e in enumerate(self.entries):
            if e.id == target_id:
                deleted = self.entries.pop(i)
                self.save()
                print(f"Deleted diary {target_id}.  {deleted.title}.")
                return
        print(f"Diary ID {target_id} was not found :( " )

    def search_entries(self):
        print("\n+=+=+= Search Diary =+=+=+")
        query = input("Enter keyword or mood to search: ").strip().lower()
        if not query:
            return

        results = [e for e in self.entries if query in e.title.lower() or query in e.content.lower() or query in e.mood.lower()]
        self.view(results)

    def run(self):
        while True:
            print("\nDear Diary...")
            time.sleep(3)
            print("1. Write new entry\n2. View all entries\n3. Search entries\n4. Edit an entry\n5. Delete an entry\n6. Exit")
            choice = input("\nChoose an option(1-6) ").strip()

            if choice == "1":
                self.create_entry()
            elif choice == "2":
                self.view()
            elif choice == "3":
                self.search_entries()
            elif choice == "4":
                self.update()
            elif choice == "5":
                self.delete_entry()
            elif choice == "6":
                print("\nGoodbye! Your thoughts are safe on disk.")
                break
            else:
                print("Invalid option. Please enter a number between 1 and 6.")

diary = DearDiary()
diary.run()