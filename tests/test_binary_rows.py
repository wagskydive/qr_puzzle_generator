from core.binary_rows import BinaryRows

def test_rows_generation_and_check():
    puzzle = BinaryRows([('1+1', 2), ('2+1', 3)])
    assert puzzle.expected_rows() == ['10', '11']
    assert puzzle.check_row(0, '10')
    assert not puzzle.check_row(1, '10')
