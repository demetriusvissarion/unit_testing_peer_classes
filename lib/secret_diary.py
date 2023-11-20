class SecretDiary:
    def __init__(self, diary):
        # diary is an instance of Diary
        self.diary = diary
        self.diary_lock = True

    def read(self):
        # Raises the error "Go away!" if the diary is locked
        # Returns the diary's contents if the diary is unlocked
        # The diary starts off locked
        if self.diary_lock == True:
            raise Exception("Go away!") 
        else:
            return self.diary.read()

    def lock(self):
        # Locks the diary
        # Returns nothing
        self.diary_lock = True

    def unlock(self):
        # Unlocks the diary
        # Returns nothing
        self.diary_lock = False