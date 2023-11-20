import pytest
from lib.diary import *
from lib.secret_diary import *

"""
Given an instance of the class with diary, and diary is unlocked
#read Returns the contents of the diary
"""
def test_if_reads_diary():
    diary = Diary('15/11/2023 Gym: Completed upper body day 1 weightlifting program today')
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    result = secret_diary.read()
    assert result == '15/11/2023 Gym: Completed upper body day 1 weightlifting program today'


"""
Given an instance of the class with diary, and diary is locked
#read throws an error
"""
def test_if_reads_throws_an_error_when_locked():
    diary = Diary('15/11/2023 Gym: Completed upper body day 1 weightlifting program today')
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    secret_diary.lock()
    with pytest.raises(Exception) as e: 
        secret_diary.read()
    error_message = str(e.value)
    assert error_message == "Go away!"