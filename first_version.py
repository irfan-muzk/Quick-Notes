class Note:
    def __init__(self):
        self.title = ""
        self.notes = ""

    def ask_title(self):
        self.title = input("Type The title: ")

    def ask_notes(self):
        self.notes = input("Type The Notes: ")

    def show_result(self):
        print(f"title = {self.title}\nnotes: {self.notes}")

    def save_notes(self):
        filename = "save_note.txt"
        with open(filename, "a") as save:
            save.write(f"\ntitle = {self.title}\nnotes: {self.notes}\n")

user = Note()

user.ask_title()
user.ask_notes()
user.show_result()
user.save_notes()