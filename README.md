# IDS-Rule-Gen

## Giới thiệu

IDS-Rule-Gen là công cụ tự động hóa bảo mật được viết bằng Python, dùng để chuyển đổi Threat Intelligence (danh sách IP độc hại) thành rule cho hệ thống IDS như Suricata và Snort.

Mục tiêu của dự án là hỗ trợ SOC Analyst hoặc Security Engineer giảm thao tác thủ công khi tạo rule IDS từ IOC (Indicator of Compromise), giúp tăng tốc độ phát hiện mối đe dọa trong hệ thống mạng.

---

# Chức năng chính

- Đọc danh sách IP độc hại từ file CSV
- Kiểm tra IP IPv4 hợp lệ
- Loại bỏ IP lỗi hoặc trùng lặp
- Sinh rule đúng định dạng Suricata/Snort
- Tự động tăng SID cho mỗi rule
- Làm sạch description để tránh lỗi syntax
- Xuất file `.rules`
- Hỗ trợ unit test để kiểm tra tính đúng đắn
---

## ⚙️ Yêu cầu hệ thống

* Python >= 3.8
* Linux / Windows / macOS

---

## 📦 Cài đặt (QUAN TRỌNG)

⚠️ Trên Kali Linux, bạn **không thể dùng pip trực tiếp**, cần tạo môi trường ảo.

### 🔹 Bước 1: Clone project

```bash
git clone <your-repo-url>
cd IDS-Rule-Gen
```

---

### 🔹 Bước 2: Tạo virtual environment

```bash
python3 -m venv venv
```

Nếu lỗi, cài thêm:

```bash
sudo apt install python3-venv
```

---

### 🔹 Bước 3: Kích hoạt môi trường

```bash
source venv/bin/activate
```

👉 Khi thành công sẽ thấy:

```bash
(venv) user@machine:~/IDS-Rule-Gen$
```

---

### 🔹 Bước 4: Cài thư viện

```bash
pip install -r requirements.txt
```

---

## ▶️ Cách chạy chương trình

```bash
python3 -m src.main --input data/sample_ips.csv --output data/output.rules
```

👉 Kết quả:

* In ra: `Đã tạo thành công X rules`
* Tạo file `data/output.rules`

---

## 📥 Định dạng input

File CSV:

```csv
ip,description
192.168.1.1,Cobalt Strike
8.8.8.8,DNS Malware
```

---

## 📤 Output

Ví dụ rule:

```text
alert ip $EXTERNAL_NET 192.168.1.1 -> $HOME_NET any (msg:'Blacklisted IP: Cobalt Strike'; sid:1000001; rev:1;)
```

---

## 🧪 Chạy Unit Test

```bash
python3 -m unittest discover tests
```

👉 Kết quả mong đợi:

```
..
----------------------------------------------------------------------
Ran 2 tests

OK
```

---

## ⚡ Test nhanh cho người chấm

Chỉ cần chạy:

```bash
# setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# test
python3 -m unittest discover tests

# run
python3 -m src.main --input data/sample_ips.csv --output data/output.rules
```

👉 Nếu:

* Test PASS
* Có file output.rules

→ Project hoạt động đúng

---

## ⚠️ Xử lý lỗi

* IP sai → bị bỏ qua
* File không tồn tại → báo lỗi
* CSV sai format → không xử lý

---

## 📂 Cấu trúc dự án

```
IDS-Rule-Gen/
├── config.yaml
├── data/
│   └── sample_ips.csv
├── src/
│   ├── main.py
│   ├── parser.py
│   ├── rule_generator.py
│   └── utils.py
├── tests/
│   ├── test_parser.py
│   └── test_rule_generator.py
├── requirements.txt
└── README.md
```

---

## 🚀 Hướng phát triển

* Hỗ trợ domain / port
* Tích hợp Threat Intelligence API
* Logging ra file
* Đóng gói CLI (pip install)

---

## 👤 Tác giả

* Thanh – Cybersecurity Student

---

## 📄 License

Dự án phục vụ mục đích học tập

