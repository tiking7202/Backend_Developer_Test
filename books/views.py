from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .models import Book
from .serializers import BookSerializer
from django.shortcuts import get_object_or_404

class BookViewSet(viewsets.ViewSet):
    
    # Lấy danh sách tất cả các cuốn sách
    def list(self, request):
        books = Book.objects.all()  # Truy vấn tất cả các bản ghi sách trong cơ sở dữ liệu
        serializer = BookSerializer(books, many=True)  # Chuyển đổi dữ liệu sách thành dạng JSON
        return Response(serializer.data)  # Trả về dữ liệu JSON của danh sách sách

    # Tạo một cuốn sách mới
    def create(self, request):
        serializer = BookSerializer(data=request.data)  # Tạo serializer với dữ liệu từ yêu cầu
        
        # Kiểm tra các trường bắt buộc
        if 'title' not in request.data or not request.data['title']:
            return Response({"error": "Title is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        if 'author' not in request.data or not request.data['author']:
            return Response({"error": "Author is required."}, status=status.HTTP_400_BAD_REQUEST)

        if 'published_date' not in request.data or not request.data['published_date']:
            return Response({"error": "Published date is required."}, status=status.HTTP_400_BAD_REQUEST)

        if 'isbn' not in request.data or not request.data['isbn']:
            return Response({"error": "ISBN is required."}, status=status.HTTP_400_BAD_REQUEST)

        if 'price' not in request.data or not request.data['price']:
            return Response({"error": "Price is required."}, status=status.HTTP_400_BAD_REQUEST)

        # Kiểm tra tính duy nhất của isbn
        if Book.objects.filter(isbn=request.data['isbn']).exists():
            return Response({"error": "ISBN already exists."}, status=status.HTTP_400_BAD_REQUEST)

        # Kiểm tra tính hợp lệ và lưu nếu không có lỗi
        if serializer.is_valid():
            serializer.save()  # Lưu sách mới vào cơ sở dữ liệu
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Trả về dữ liệu sách mới
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Trả về lỗi nếu có

    # Lấy thông tin của một cuốn sách cụ thể dựa trên id
    def retrieve(self, request, pk=None):
        book = get_object_or_404(Book, pk=pk)  # Tìm cuốn sách hoặc trả về lỗi 404 nếu không tìm thấy
        serializer = BookSerializer(book)  # Chuyển đổi dữ liệu sách thành dạng JSON
        return Response(serializer.data)  # Trả về dữ liệu JSON của sách

    # Cập nhật thông tin của một cuốn sách
    def update(self, request, pk=None):
        book = get_object_or_404(Book, pk=pk)  # Tìm cuốn sách hoặc trả về lỗi 404 nếu không tìm thấy
        serializer = BookSerializer(book, data=request.data)  # Tạo serializer với dữ liệu cập nhật từ yêu cầu

        # Kiểm tra các trường bắt buộc
        if 'title' not in request.data or not request.data['title']:
            return Response({"error": "Title is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        if 'author' not in request.data or not request.data['author']:
            return Response({"error": "Author is required."}, status=status.HTTP_400_BAD_REQUEST)

        if 'published_date' not in request.data or not request.data['published_date']:
            return Response({"error": "Published date is required."}, status=status.HTTP_400_BAD_REQUEST)

        if 'isbn' not in request.data or not request.data['isbn']:
            return Response({"error": "ISBN is required."}, status=status.HTTP_400_BAD_REQUEST)

        if 'price' not in request.data or not request.data['price']:
            return Response({"error": "Price is required."}, status=status.HTTP_400_BAD_REQUEST)

        # Kiểm tra tính duy nhất của isbn nếu isbn được thay đổi
        if request.data.get('isbn') != book.isbn and Book.objects.filter(isbn=request.data['isbn']).exists():
            return Response({"error": "ISBN already exists."}, status=status.HTTP_400_BAD_REQUEST)

        # Kiểm tra tính hợp lệ và lưu nếu không có lỗi
        if serializer.is_valid():
            serializer.save()  # Lưu thông tin sách cập nhật vào cơ sở dữ liệu
            return Response(serializer.data)  # Trả về dữ liệu sách đã cập nhật
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Trả về lỗi nếu có

    # Xóa một cuốn sách cụ thể dựa trên id
    def destroy(self, request, pk=None):
        book = get_object_or_404(Book, pk=pk)  # Tìm cuốn sách hoặc trả về lỗi 404 nếu không tìm thấy
        book.delete()  # Xóa sách khỏi cơ sở dữ liệu
        return Response(status=status.HTTP_204_NO_CONTENT)  # Trả về phản hồi thành công với mã 204

