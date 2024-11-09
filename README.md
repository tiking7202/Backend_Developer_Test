Bookstore API
Dự án này là một API quản lý sách đơn giản, sử dụng Django và PostgreSQL. API cho phép người dùng thực hiện các thao tác CRUD (Tạo, Đọc, Cập nhật, Xóa) đối với dữ liệu sách.

Mục Lục
Giới Thiệu
Cài Đặt Môi Trường
Cấu Hình Cơ Sở Dữ Liệu
Cài Đặt Ứng Dụng
Chạy Ứng Dụng
Các Endpoint
Kiểm Tra API

API này quản lý thông tin sách với các trường sau:
id (Primary Key)
title (String)
author (String)
published_date (Date)
isbn (String, unique)
price (Decimal)
Các API sẽ cho phép bạn thực hiện các thao tác CRUD (Create, Read, Update, Delete) đối với sách trong cơ sở dữ liệu PostgreSQL.

Cài Đặt Môi Trường
1. Cài Đặt Python
Đảm bảo rằng bạn đã cài đặt Python 3.x. Nếu chưa, bạn có thể tải Python từ python.org.

2. Cài Đặt Django
Cài đặt Django bằng lệnh pip: pip install django

4. Cài Đặt Django REST Framework
Để xử lý các yêu cầu API, chúng ta sẽ sử dụng Django REST Framework: pip install djangorestframework

6. Cài Đặt PostgreSQL
Cài đặt PostgreSQL và tạo một cơ sở dữ liệu mới. Hướng dẫn cài đặt có thể tìm thấy tại PostgreSQL Official.

7. Cài Đặt Psycopg2 (Kết Nối PostgreSQL)
Cài đặt thư viện psycopg2 để kết nối Django với PostgreSQL: pip install psycopg2

8. Cài đặt các module cần thiết để chạy dự án
   
Cấu Hình Cơ Sở Dữ Liệu
Tạo Cơ Sở Dữ Liệu: Truy cập vào PostgreSQL và tạo một cơ sở dữ liệu mới:  CREATE DATABASE bookstore;

Cấu Hình Cơ Sở Dữ Liệu trong Django: Mở file bookstore/settings.py và cấu hình phần cơ sở dữ liệu như sau:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bookstore',
        'USER': 'yourusername',  # Thay bằng tên người dùng PostgreSQL của bạn
        'PASSWORD': 'yourpassword',  # Thay bằng mật khẩu của bạn
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

Cài Đặt Ứng Dụng
Tạo Dự Án Django: django-admin startproject bookstore

Tạo Ứng Dụng "Books":
python manage.py startapp books
Mở file bookstore/settings.py và thêm 'books' vào danh sách INSTALLED_APPS:

Chạy Ứng Dụng
Migrate Cơ Sở Dữ Liệu:
Chạy lệnh migrate để tạo bảng trong cơ sở dữ liệu:
python manage.py makemigrations
python manage.py migrate

Chạy Máy Chủ Django:
Chạy ứng dụng Django bằng lệnh sau: python manage.py runserver
Máy chủ sẽ được chạy tại http://127.0.0.1:8000/.

Các Endpoint
1. Tạo Sách Mới (Create)
Đường Dẫn: POST: http://127.0.0.1:8000//api/books/
Ví Dụ Dữ Liệu:
{
  "title": "Sách Mới",
  "author": "Tác Giả",
  "published_date": "2024-11-01",
  "isbn": "1234567890123",
  "price": 100.00
}
2. Lấy Thông Tin Chi Tiết Một Cuốn Sách Theo Id (Read)
Đường Dẫn: GET:  http://127.0.0.1:8000//api/books/{id}/
3. Lấy Danh Sách Sách (Read All)
Đường Dẫn: GET:  http://127.0.0.1:8000//api/books/
Mô Tả: Lấy danh sách tất cả sách.
4. Cập Nhật Thông Tin Sách (Update)
Đường Dẫn: PUT:  http://127.0.0.1:8000//api/books/{id}/
5. Xóa Sách Theo Id (Delete)
Đường Dẫn: DELETE: http://127.0.0.1:8000//api/books/{id}/

Kiểm Tra API
Bạn có thể kiểm tra API bằng các công cụ như Postman hoặc cURL.
