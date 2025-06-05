
# 💧 Đề tài: Cảm Biến Lưu Lượng Nước – Hệ Thống Giám Sát Tự Động với ESP32

📘 **Môn học:** Thành phố Thông minh và Nông nghiệp Thông minh  
👨‍🎓 **Sinh viên:** Nguyễn Minh Đức – 1571020068  
🏫 **Trường:** Đại học Đại Nam  
👨‍🏫 **GVHD:** ThS. Trần Đăng Công  
📅 **Năm:** 2025

---

## 🎯 Mục tiêu đề tài

- ✅ Đo lưu lượng và thể tích nước chảy qua bằng cảm biến xung (YF-S201).
- 📡 Gửi dữ liệu từ ESP32 về server Flask qua WiFi.
- 📈 Hiển thị dữ liệu trên web/server và đưa ra cảnh báo khi vượt ngưỡng.
- 🛑 Tự động ngắt máy bơm khi thể tích vượt quá mức giới hạn.

---

## ⚙️ Công nghệ sử dụng

| Thành phần         | Mô tả |
|-------------------|------|
| 💻 Vi điều khiển   | ESP32 DevKit V1 |
| 🔄 Cảm biến         | Lưu lượng nước YF-S201 hoặc SEN-HZ21WA |
| 🌐 Giao tiếp        | WiFi (HTTP POST) |
| 🧠 Phần mềm         | Arduino IDE, Flask (Python) |
| 🖥️ Giao diện server | Flask log terminal hoặc mở rộng bằng dashboard |
| ⚙️ Điều khiển        | Relay Module để bật/tắt máy bơm |

---

## 📂 Cấu trúc thư mục dự án

```
CamBien_LuuLuong_Nuoc/
├── arduino/
│   └── flow_sensor_esp32.ino
├── server/
│   └── app.py
├── README.md
└── requirements.txt
```

---

## 🚀 Hướng dẫn sử dụng

### 1. ESP32 Arduino

- Sửa `ssid`, `password`, `serverURL` trong `flow_sensor_esp32.ino`
- Flash code lên ESP32 bằng Arduino IDE
- Kết nối cảm biến lưu lượng (D4) và Relay điều khiển bơm (D5)

### 2. Flask server

```bash
cd server
pip install -r ../requirements.txt
python app.py
```

- Mở địa chỉ `http://<IP-của-server>:5000` để kiểm tra log dữ liệu đến

---

## 📊 Kết quả kỳ vọng

- 📉 Sai số đo < 5% ở dải 1–30 L/phút  
- 📶 Gửi dữ liệu mỗi giây lên server ổn định  
- 💾 Ghi nhận tổng thể tích và cảnh báo khi vượt ngưỡng  
- 🔌 Tự động tắt bơm khi thể tích vượt 2000L

---

## 📚 Tài liệu tham khảo

- [ESP32 Documentation](https://docs.espressif.com/)
- [YF-S201 Datasheet](https://cdn.sparkfun.com/datasheets/Sensors/Flow/YF-S201.pdf)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Arduino Reference](https://www.arduino.cc/reference/en/)

---

> 🔐 *Dự án mô phỏng hệ thống giám sát và điều khiển nước trong nông nghiệp thông minh, hướng tới tối ưu tài nguyên và tự động hóa.*

---

🎉 *Cảm ơn bạn đã xem!*
