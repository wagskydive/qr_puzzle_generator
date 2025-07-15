from qr_processor import generate_matrix, load_matrix
import qrcode


def test_generate_matrix():
    matrix = generate_matrix("test")
    assert isinstance(matrix, list)
    assert all(isinstance(row, list) for row in matrix)
    assert all(cell in (0, 1) for row in matrix for cell in row)


def test_load_matrix(tmp_path):
    qr = qrcode.QRCode(border=0, box_size=1)
    qr.add_data("test")
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    path = tmp_path / "code.png"
    img.save(path)

    loaded = load_matrix(str(path))
    expected = qr.get_matrix()
    assert loaded == expected
