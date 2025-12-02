from pathlib import Path
from .solution import main

TEST_INPUT = Path(__file__).parent / 'test_input.txt'

"""
Test for part 1
"""
def test_zero_count_calculation():
   
    expected_output = 3 
    assert expected_output == main(TEST_INPUT)[0]

"""
Test for part 2
"""
def test_total_zero_pass_calculation():
    
    expected_output = 6
    assert expected_output == main(TEST_INPUT)[1]