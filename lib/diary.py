class Diary:
    def __init__(self, contents):
        # contents is a string
        if contents == None or len(contents) <= 0:
            raise Exception("Invalid entry, 'contents' must have at least one character.")
        else:
            self.diary_contents = contents

    def read(self):
        # Returns the contents of the diary
        return self.diary_contents