import csv
import os
from src.utils import is_valid_ip


def load_csv(file_path: str):
    """
    Đọc file CSV chứa danh sách IP và description.
    Chỉ trả về các IP hợp lệ.

    Args:
        file_path (str): Đường dẫn tới file CSV

    Returns:
        list[dict]: Danh sách các IP hợp lệ dạng:
                    [{"ip": "...", "description": "..."}]
    """

    if not os.path.exists(file_path):
        print(f"[ERROR] File not found: {file_path}")
        return []

    valid_entries = []

    try:
        with open(file_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)

            # Kiểm tra header hợp lệ
            if "ip" not in reader.fieldnames or "description" not in reader.fieldnames:
                print("[ERROR] Invalid CSV format. Required columns: 'ip', 'description'")
                return []

            for line_num, row in enumerate(reader, start=2):  # start=2 vì dòng 1 là header
                ip = row.get("ip", "").strip()
                desc = row.get("description", "").strip()

                if not ip:
                    print(f"[WARNING] Missing IP at line {line_num}, skipping...")
                    continue

                if not is_valid_ip(ip):
                    print(f"[WARNING] Invalid IP '{ip}' at line {line_num}, skipping...")
                    continue

                valid_entries.append({
                    "ip": ip,
                    "description": desc
                })

        if not valid_entries:
            print("[INFO] No valid IP entries found in file.")

        return valid_entries

    except Exception as e:
        print(f"[ERROR] Failed to read CSV file: {e}")
        return []

