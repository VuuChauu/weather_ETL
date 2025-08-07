# Weather ETL Project ☁️

Pipeline ETL thu thập dữ liệu thời tiết từ OpenWeather API, xử lý và lưu vào BigQuery bằng Python.

## Features
- Extract: Lấy dữ liệu thời tiết từ API
- Transform: Làm sạch dữ liệu
- Load: Upload lên BigQuery
- Configurable qua `cities.json`
- Code tổ chức rõ ràng theo thư mục `etl/`

## Hướng dẫn chạy
```bash
pip install -r requirements.txt
python test.py
