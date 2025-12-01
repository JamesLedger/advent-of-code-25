from day_1.solution import main

expected_output = 3

"""
This test uses the example input with the expected output taken from challenge.md to ensure the answer is calculated correctly
"""
def test_zero_count_calculation():
    
    assert expected_output == main('day_1/test_input.txt')

