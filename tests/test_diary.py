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