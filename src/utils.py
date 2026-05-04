import ipaddress
import re


def is_valid_ip(ip: str) -> bool:
    """
    Kiểm tra một chuỗi có phải là IPv4 hợp lệ hay không.

    Args:
        ip (str): Chuỗi IP cần kiểm tra

    Returns:
        bool: True nếu hợp lệ, False nếu không
    """
    try:
        ip_obj = ipaddress.ip_address(ip)
        return isinstance(ip_obj, ipaddress.IPv4Address)
    except ValueError:
        return False


def format_msg(text: str) -> str:
    """
    Làm sạch nội dung message để tránh lỗi khi đưa vào rule Suricata.

    - Loại bỏ ký tự đặc biệt nguy hiểm: ; " ' \ ( ) { }
    - Giữ lại chữ, số, khoảng trắng và một số ký tự an toàn
    - Trim khoảng trắng dư

    Args:
        text (str): Chuỗi mô tả ban đầu

    Returns:
        str: Chuỗi đã được làm sạch
    """

    if not text:
        return ""

    # Loại bỏ các ký tự có thể phá vỡ syntax rule
    text = re.sub(r'[;"\'\\\(\)\{\}]', '', text)

    # Chỉ giữ lại ký tự an toàn (chữ, số, space, ., -, _)
    text = re.sub(r'[^a-zA-Z0-9\s\.\-_]', '', text)

    # Chuẩn hóa khoảng trắng
    text = re.sub(r'\s+', ' ', text).strip()

    return text
