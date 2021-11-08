from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from .forms import GenerateRandomUserForm
from .serializers import TestSerializer
from .tasks import create_random_user_accounts
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response


class UsersListView(ListView):
    template_name = 'core/users_list.html'
    model = User


class GenerateRandomUserView(FormView):
    template_name = 'core/generate_random_users.html'
    form_class = GenerateRandomUserForm

    def form_valid(self, form):
        total = form.cleaned_data.get('total')
        create_random_user_accounts.delay(total)
        messages.success(self.request, 'We are generating your random users! Wait a moment and refresh this page.')
        return redirect('users_list')


class TestAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = TestSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        param = serializer.data
        create_random_user_accounts.delay(param['total'])
        messages.success(self.request, 'We are generating your random users! Wait a moment and refresh this page.')

        headers = self.get_success_headers(serializer.data)
        return Response({"result": "true"}, status=status.HTTP_200_OK, headers=headers)
