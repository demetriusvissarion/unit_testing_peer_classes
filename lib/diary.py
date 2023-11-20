class Diary:
    def __init__(self, contents):
        # contents is a string
        self.diary_contents = contents

    def read(self):
        # Returns the contents of the diary
        return self.diary_contents