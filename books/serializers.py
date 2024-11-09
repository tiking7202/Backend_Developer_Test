from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        extra_kwargs = {
            'isbn': {'validators': []},
            'price': {'min_value': 0}
        }

    # Tùy chỉnh kiểm tra giá trị cho trường ISBN
    def validate_isbn(self, value):
        if len(value) != 13:
            raise serializers.ValidationError("ISBN phải có 13 ký tự.")
        return value