from rest_framework import serializers


class TestSerializer(serializers.Serializer):
    total = serializers.IntegerField(allow_null=True, required=False)
