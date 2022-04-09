from rest_framework import serializers

from common.utils import get_fibonacci_value_recursive


class FibonacciSerializer(serializers.Serializer):
    number = serializers.CharField(required=True)
    fibonacci = serializers.SerializerMethodField()

    def get_fibonacci(self, obj):
        number = int(obj.get('number', 0))
        return get_fibonacci_value_recursive(number)
