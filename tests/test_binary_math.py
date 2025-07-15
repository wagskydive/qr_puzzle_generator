from core.binary_math import BinaryMath

def test_binary_math():
    puzzle = BinaryMath('2+2', 4)
    assert puzzle.expected_pattern() == '100'
    assert puzzle.check_answer('100')
    assert puzzle.check_answer('0100')
    assert not puzzle.check_answer('101')
