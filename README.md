# Hệ Thống Quản Lý Học Sinh

Một ứng dụng quản lý học sinh hoàn toàn với giao diện Tkinter và cơ sở dữ liệu MySQL.

## Yêu Cầu

- Python 3.7+
- MySQL Server 5.7+
- Các thư viện Python:
  - `mysql-connector-python`
  - `tkinter` (thường được cài đặt sẵn với Python)

## Thiết Lập

### 1. Cài Đặt Dependencies

```bash
pip install mysql-connector-python
```

### 2. Khởi Tạo Cơ Sở Dữ Liệu

Trước tiên, chạy file `setup_database.py` để tạo cơ sở dữ liệu và các bảng:

```bash
python setup_database.py
```

Điều này sẽ:

- Tạo database `student_management`
- Tạo 9 bảng cần thiết
- Chèn dữ liệu mặc định (roles, grade_levels, subjects)

### 3. Chạy Ứng Dụng

Sau khi cơ sở dữ liệu được thiết lập, chạy file `hello_world.py`:

```bash
python hello_world.py
```

## Thông Tin Kết Nối Cơ Sở Dữ Liệu

- **Host**: localhost
- **User**: root
- **Password**: 123456
- **Database**: student_management

## Tài Khoản Mặc Định

Hệ thống không có tài khoản mặc định. Bạn cần đăng ký một tài khoản mới để bắt đầu:

1. Nhấn nút "Đăng ký tài khoản" trên giao diện đăng nhập
2. Điền thông tin:
   - Họ tên
   - Tài khoản (tên đăng nhập)
   - Mật khẩu
   - Vai trò:
     - **Quản trị viên**: Xem báo cáo tổng hợp
     - **Giáo viên**: Quản lý lớp, điểm danh, xem học sinh
     - **Học sinh**: Xem điểm danh cá nhân

## Chức Năng Chính

### Quản Trị Viên

- Xem báo cáo tổng hợp (số học sinh, giáo viên, lớp)
- Quản lý tài khoản người dùng
- Xem thống kê hệ thống

### Giáo Viên

- Quản lý lớp học
- Ghi điểm danh học sinh
- Xem danh sách học sinh
- Xem phân công giáo viên
- Xuất báo cáo

### Học Sinh

- Xem thông tin điểm danh cá nhân
- Tự điểm danh
- Xem lịch sử điểm danh

## Cấu Trúc Cơ Sở Dữ Liệu

- **roles**: Vai trò người dùng (Quản trị, Giáo viên, Học sinh)
- **users**: Thông tin người dùng
- **grade_levels**: Khối lớp (6, 7, 8, 9)
- **classes**: Lớp học
- **students**: Thông tin học sinh
- **subjects**: Môn học
- **teaching_assignments**: Phân công giáo viên
- **grades**: Điểm số học sinh
- **attendance**: Điểm danh

## Khắc Phục Sự Cố

### Lỗi kết nối MySQL

- Đảm bảo MySQL Server đang chạy
- Kiểm tra thông tin kết nối trong `hello_world.py` và `setup_database.py`
- Mật khẩu mặc định là: `123456`

### Lỗi "database not found"

- Chạy `setup_database.py` để tạo cơ sở dữ liệu
- Nếu vẫn không hoạt động, xóa database cũ và chạy lại

### Lỗi Tkinter không tìm thấy

- Cài đặt tkinter: `pip install tk`

## Ghi Chú

- Mọi thay đổi dữ liệu được lưu trực tiếp vào cơ sở dữ liệu
- Điểm danh được ghi nhận với thời gian hiện tại
- Người ghi nhận điểm danh được lưu vào database

## Hỗ Trợ

Nếu bạn gặp vấn đề, vui lòng kiểm tra:

1. MySQL Server có đang chạy
2. Cơ sở dữ liệu `student_management` tồn tại
3. Bảng `users` có chứa tài khoản
4. Thông tin kết nối trong code
