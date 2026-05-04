import argparse
import sys
import os

from src.parser import load_csv
from src.rule_generator import SuricataGenerator


def main():
    parser = argparse.ArgumentParser(
        description="IDS-Rule-Gen: Generate Suricata rules from CSV IP list"
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Path to input CSV file (e.g., data/sample_ips.csv)"
    )

    parser.add_argument(
        "--output",
        required=True,
        help="Path to output rules file (e.g., data/output.rules)"
    )

    args = parser.parse_args()

    input_path = args.input
    output_path = args.output

    # Kiểm tra file input tồn tại
    if not os.path.exists(input_path):
        print(f"[ERROR] Input file not found: {input_path}")
        sys.exit(1)

    # 1. Load dữ liệu
    entries = load_csv(input_path)

    if not entries:
        print("[INFO] No valid data to process. Exiting.")
        sys.exit(0)

    # 2. Generate rules
    generator = SuricataGenerator()
    rules = generator.generate_rules(entries)

    # 3. Ghi file output
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            for rule in rules:
                f.write(rule + "\n")
    except Exception as e:
        print(f"[ERROR] Failed to write output file: {e}")
        sys.exit(1)

    # 4. Tổng kết
    print(f"Đã tạo thành công {len(rules)} rules")


if __name__ == "__main__":
    main()
