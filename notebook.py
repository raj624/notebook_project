from note import Note


class Notebook:
    """initialise a notebook with an empty note as list"""
    def __init__(self):
        self.notes = []

    def new_note(self, memo, tags=""):
        """create a note and add to the notebook list"""
        self.notes.append(Note(memo, tags))

    def _find_note(self, note_id):
        """locate the note in the notebook with the given note_id"""
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
            return None

    def modify_note(self, note_id, new_memo):
        """find the note with the note_id and modify the memo part of the note"""
        note = self._find_note(note_id)
        if note:
            note.memo = new_memo
            return True
        return False

    def modify_tag(self, note_id, new_tags):
        """find the note with the note_id and modify the tags part of the note"""
        note = self._find_note(note_id)
        if note:
            note.tags = new_tags
            return True
        return False

    def display_note(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                return 'Memo: {} Tags : {}'.format(note.memo, note.tags)

    def search(self, filter_txt):
        """find all the notes from notebook with matching memo or tags"""
        return [note for note in self.notes if note.match(filter_txt)]
