import pytest
from lib.diary import *

"""
Given an instance of the class with contents
#read Returns the contents of the diary
"""
def test_if_reads_diary():
    diary = Diary('15/11/2023 Gym: Completed upper body day 1 weightlifting program today')
    result = diary.read()
    assert result == '15/11/2023 Gym: Completed upper body day 1 weightlifting program today'


"""
Given an instance of the class without contents
#read throws an error
"""
def test_if_throws_error_when_empty_argument():
    with pytest.raises(Exception) as e: 
        Diary('')
    error_message = str(e.value)
    assert error_message == "Invalid entry, 'contents' must have at least one character."