
# 💧 Đề tài: Cảm Biến Lưu Lượng Nước – Hệ Thống Giám Sát Tự Động với ESP32

📘 **Môn học:** Thành phố Thông minh và Nông nghiệp Thông minh  
👨‍🎓 **Sinh viên:** Nguyễn Minh Đức – 1571020068  
🏫 **Trường:** Đại học Đại Nam  
👨‍🏫 **GVHD:** ThS. Trần Đăng Công  
📅 **Năm:** 2025

---

## 🎯 Mục tiêu đề tài

- ✅ Thiết kế hệ thống **giám sát lưu lượng nước** sử dụng cảm biến giá rẻ nhưng chính xác.
- 📡 Gửi dữ liệu đo được **về máy chủ qua WiFi** theo thời gian thực.
- 📈 Tính toán **tổng thể tích nước sử dụng**, cảnh báo khi vượt ngưỡng.
- 🛑 Tự động **ngắt máy bơm** khi lưu lượng vượt quá mức giới hạn cho phép.

---

## ⚙️ Công nghệ sử dụng

| Thành phần        | Công nghệ |
|------------------|-----------|
| 💻 Vi điều khiển  | ESP32 DevKit V1 |
| 🔄 Cảm biến       | Cảm biến lưu lượng nước YF-S201 / SEN-HZ21WA |
| 🌐 Giao tiếp      | WiFi (ESP32 → HTTP POST về server Flask) |
| 🧠 Phần mềm       | Arduino IDE, Flask Server, Python |
| 📊 Giao diện      | Web/App hiển thị dữ liệu đo theo thời gian thực |
| 🔌 Điều khiển     | Relay Module điều khiển bơm nước |

---

## 🧪 Kết quả thử nghiệm

- 📉 **Sai số đo < 5%** ở dải 1–30 L/phút  
- 📶 **Kết nối WiFi ổn định**, truyền dữ liệu đều đặn  
- 💡 **Tự động ngắt máy bơm** khi vượt ngưỡng 2000L  
- 💾 **Lưu trữ dữ liệu** trên server để phân tích sau

---

## 💡 Kiến nghị triển khai

- 🚜 Ứng dụng trong **nông nghiệp thông minh** để tối ưu lượng nước tưới.  
- 🏠 Dùng trong **nhà thông minh** giám sát rò rỉ nước và cảnh báo sớm.  
- 🏭 Tích hợp với **hệ thống quản lý nguồn nước công nghiệp**.  
- 📱 Mở rộng tích hợp với app điều khiển từ xa & cảnh báo qua điện thoại.

---

## 📚 Tài liệu tham khảo

- [ESP32 Documentation](https://docs.espressif.com/)
- [Arduino Reference](https://www.arduino.cc/reference/en/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- Datasheet cảm biến YF-S201, SEN-HZ21WA
- Tạp chí Khoa học & Công nghệ Môi trường

---

> 🔐 *Dự án này là mô hình thử nghiệm thực tiễn trong lĩnh vực nông nghiệp – đô thị thông minh, hướng đến tiết kiệm tài nguyên và bảo vệ môi trường.*

---

🎉 *Cảm ơn bạn đã đọc!*
