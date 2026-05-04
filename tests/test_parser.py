import os
import tempfile
import unittest

from src.parser import load_csv


def test_invalid_ip_filtered():
    """
    Kiểm tra IP sai định dạng sẽ bị loại bỏ
    """
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix=".csv") as tmp:
        tmp.write("ip,description\n")
        tmp.write("192.168.1.1,Valid IP\n")
        tmp.write("999.999.999,Invalid IP\n")
        tmp_path = tmp.name

    try:
        result = load_csv(tmp_path)

        # Chỉ giữ lại 1 IP hợp lệ
        assert len(result) == 1
        assert result[0]["ip"] == "192.168.1.1"

    finally:
        os.remove(tmp_path)


def test_empty_csv():
    """
    File CSV trống → không crash, trả về list rỗng
    """
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix=".csv") as tmp:
        tmp.write("ip,description\n")  # chỉ có header
        tmp_path = tmp.name

    try:
        result = load_csv(tmp_path)

        assert result == []

    finally:
        os.remove(tmp_path)


def test_file_not_found():
    """
    File không tồn tại → xử lý êm, không crash
    """
    fake_path = "non_existent_file.csv"

    result = load_csv(fake_path)

    assert result == []
