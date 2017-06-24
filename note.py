import datetime

# sore next available ids for notes
last_id = 0


class Note:
    """Represents the note created within a notebook"""

    def __init__(self, memo, tags=None):
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def __str__(self):
        return 'Memo: {} Tags : {}'.format(self.memo, self.tags)

    def match(self, filter_txt):
        """Determines if it matches the filter text. returns True is match is found"""
        if filter_txt in self.memo:
            return True
        elif filter_txt in self.tags:
            return True
        else:
            return False


