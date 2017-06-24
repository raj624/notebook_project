import sys
from notebook import Notebook

class Menu:
    """display a choice menu and respond when actioned an option"""
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_notes,
            "4": self.modify_notes,
            "5": self.delete_notes,
            "6": self.quit
        }

    @staticmethod
    def display_menu():
        print("""
        #### NoteBook Menu ####\n
        1. Display all Notes
        2. Search for note (memo or tag)
        3. Add a note
        4. Modify existing note
        5. Remove Notes
        6. Quit        
        """
        )

    def run(self):
        """Display the Menu and respond to choices"""
        while True:
            self.display_menu()
            choice = input("input a choice b/w 1 to 5 :")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print('{} is not a valid choice'.format(choice))

    # -->  Option(1)
    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes
        if notes:
            print("###### Notes ######")
            for note in notes:
                print('Id : {} - Memo: {} Tags : {}'.format(note.id, note.memo, note.tags))
        else:
            print("Notebook is empty..!! , Try option 3 to add note..!")

    # -->  Option(2)
    def search_notes(self):
        if not len(self.notebook.notes):
            print("Notebook is empty..!! , Try option 3 to add note..!")
            return False
        else:
            while True:
                filter_txt = input("Enter Memo or Tag for note or exit('n1') :")
                notes = self.notebook.search(filter_txt)
                if notes:
                    self.show_notes(notes)
                elif filter_txt == 'n1':
                    return False
                else:
                    print("No matching notes in notebook, Enter again..!")

    # -->  Option(3)
    def add_notes(self):
        while True:
            memo = input("Enter a memo text :")
            tag = input("Enter a Memo-Tag text :")
            if memo:
                self.notebook.new_note(memo, tag)
            else:
                print("Note input is empty..!!")
                return
            print("note is added successfully..!!")
            add = input("More notes to add (y/n) :")
            if add != 'y':
                return False

    # -->  Option(4)
    def modify_notes(self):
        while True:
            if not len(self.notebook.notes):
                print("Notebook is empty..!! , Try option 3 to add note..!")
                return False
            else:
                id = input("Enter a note id or Exit('n'):")
                try:
                    if 0 <= int(id) <= len(self.notebook.notes):
                        n_memo = input("Enter new memo text :")
                        n_tag = input("Enter new memo-Tag :")
                        if n_memo:
                            self.notebook.modify_note(id, n_memo)
                        if n_tag:
                            self.notebook.modify_tag(id, n_tag)
                        print("The note has been modified..!!")
                    else:
                        print("enter a valid id b/n (1 <= {})".format(len(self.notebook.notes)))
                except ValueError:
                    return False

    # -->  Option(5)
    def delete_notes(self):
        if not len(self.notebook.notes):
            print("Notebook is empty..!! , Try option 3 to add note..!")
            return False
        else:
            while True:
                try:
                    id = input("Enter a note id or Exit('n'):")
                    if 0 <= int(id):
                        for note in self.notebook.notes:
                            if note.id == int(id):
                                ind = self.notebook.notes.index(note)
                                val = self.notebook.notes.pop(ind)
                                print("{} : Deleted".format(val))
                    else:
                        print("enter a valid note_id")
                except ValueError:
                    return False


    # -->  Option(6)
    def quit(self):
        print("Thank you..!!")
        sys.exit(0)

if __name__ == '__main__':
    Menu().run()