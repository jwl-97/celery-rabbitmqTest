from django.contrib.auth.models import User
from django.contrib import messages
from .models import Test
from .serializers import TestSerializer
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response


class TestAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = TestSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        param = serializer.data
        total = param['total']

        for i in range(total):
            test = Test()
            test.username = 'user_{}'.format(i)
            test.email = '{}@example.com'.format(test.username)
            Test.save(test)

        messages.success(self.request, 'We are generating your random users! Wait a moment and refresh this page.')

        headers = self.get_success_headers(serializer.data)
        return Response({"result": "true"}, status=status.HTTP_200_OK, headers=headers)
