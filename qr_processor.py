"""QR code processing utilities."""
from __future__ import annotations

from typing import List

from PIL import Image
import qrcode


def generate_matrix(data: str) -> List[List[int]]:
    """Return a QR code matrix (1/0) generated from ``data``."""
    qr = qrcode.QRCode(border=0)
    qr.add_data(data)
    qr.make(fit=True)
    return qr.get_matrix()


def load_matrix(path: str) -> List[List[int]]:
    """Load a QR code image from ``path`` and return a matrix of 1/0 values."""
    img = Image.open(path).convert("L")
    pixels = img.load()
    width, height = img.size
    matrix: List[List[int]] = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(1 if pixels[x, y] < 128 else 0)
        matrix.append(row)
    return matrix
